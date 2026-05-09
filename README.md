🔒 Face Recognition-based Home Security System Using Arduino


📌 Project Overview

This project implements a real-time face recognition-based home security system that integrates a Python-based OpenCV face recognition script with an Arduino UNO microcontroller. When an authorized face is detected, no alert is triggered. If an unknown person is detected, the system prompts for a password — if the password is wrong, an LED alert is triggered via Arduino over serial communication.


🛠️ Hardware Components

Arduino UNO (ATmega328P)
LED (connected to Pin 13)
Resistor (220Ω)
Jumper Wires
Breadboard
Webcam (USB)


💻 Software & Libraries

Python 3.x
OpenCV (cv2) — Face detection & template matching
PySerial — Serial communication with Arduino
Arduino IDE — For uploading the .ino sketch


⚙️ How It Works

The webcam captures live frames continuously.
Each frame is converted to grayscale and compared against stored face templates using OpenCV Template Matching (cv2.TM_CCOEFF_NORMED).
If the match confidence exceeds the threshold (0.8), the person is identified as known — Arduino receives '0' (no alert).
If the face is unknown, the terminal prompts for a password:
Correct password → Arduino receives '0' (no alert)
Wrong password → Arduino receives '1' → LED blinks 5 times as an alert
Recognized name (or "Face Detected") is overlaid on the video feed.
