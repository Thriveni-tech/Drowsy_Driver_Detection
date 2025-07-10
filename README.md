# 🛑 Drowsy Driver Detection 🚗💤

An AI-powered real-time system to detect driver drowsiness using **OpenCV**, **Haar cascades**, and **Flask**, with sound alerts via **Pygame**.

---

## 🔍 Overview

Drowsiness while driving is a major cause of accidents. This project monitors the driver's eyes in real-time via webcam. If the eyes remain closed for a certain number of frames (indicating drowsiness), it triggers a **visual** and **audio alert**.

---

## 🎯 Features

- 👁️ Real-time face and eye detection using OpenCV Haar cascades
- ⚠️ Drowsiness score tracking and alerts
- 🔊 Audio siren using Pygame when drowsiness is detected
- 🌐 Flask-based video streaming in the browser
- 🎨 Clean UI with HTML + CSS

---

## 🛠️ Technologies Used

| Tech       | Purpose                       |
|------------|-------------------------------|
| `OpenCV`   | Face and eye detection        |
| `Flask`    | Web server and video stream   |
| `Pygame`   | Play alert siren              |
| `HTML/CSS` | Web front-end                 |

---

## 📁 Folder Structure

```plaintext
Drowsy_Driver_Detection/
│
├── static/
│   └── style.css                # Styling
│
├── templates/
│   └── index.html               # Frontend page
│
├── siren-alert-96052.mp3       # Alert sound
├── app.py                      # Main Flask + OpenCV logic
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

````

---

Prerequisites
Python 3.7 or higher

Webcam enabled device

pip (Python package manager)

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/Thriveni-tech/Drowsy_Driver_Detection.git
cd Drowsy_Driver_Detection
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have `requirements.txt`, you can install manually:

```bash
pip install flask opencv-python pygame
```

### 4. Run the Flask app

```bash
python app.py
```

Then open your browser at:
👉 `http://127.0.0.1:5000/`

---

## 🙋‍♀️ Contact

**Thriveni-tech**
📧 [thriveniravishetti@gmail.com]
🌐 [LinkedIn](https://www.linkedin.com/in/thriveni-ravishetty/)

---

