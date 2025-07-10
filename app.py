from flask import Flask, render_template, Response
import cv2
import pygame

app = Flask(__name__)

# Initialize pygame for sound alerts
pygame.mixer.init()
pygame.mixer.music.load("beep-warning-6387.mp3")  # Load your alert sound file here

# Load Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize camera
cap = cv2.VideoCapture(0)

drowsy_score = 0  # To count frames with closed eyes
drowsy_threshold = 15  # Threshold for triggering alert (score)

def play_alert():
    """Play an alert sound"""
    if not pygame.mixer.music.get_busy():  # Avoid playing multiple alerts
        pygame.mixer.music.play()

def detect_drowsiness():
    global drowsy_score

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Improve low-light conditions using adaptive histogram equalization (CLAHE)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        gray = clahe.apply(gray)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Region of interest (ROI) for detecting eyes
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Detect eyes within the face region
            eyes = eye_cascade.detectMultiScale(roi_gray)

            if len(eyes) == 0:
                drowsy_score += 1  # Increase the score when eyes are closed
            else:
                drowsy_score = 0  # Reset the score if eyes are detected

            # Draw rectangles around detected eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Display the current score on the frame
        cv2.putText(frame, f"Score: {drowsy_score}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # If eyes are closed for consecutive frames above the threshold, trigger drowsiness alert
        if drowsy_score >= drowsy_threshold:
            cv2.putText(frame, "DROWSY", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            cv2.putText(frame, "Are you Sleepy?", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
            print("Drowsy Alert!")
            play_alert()  # Play the alert sound

        # Encode the frame in JPEG format
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()

        # Use Flask's generator to continuously stream the video feed
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    """Main page."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route."""
    return Response(detect_drowsiness(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)