# IoT_Hand_Gesture_Controlled_Buzzer_Using_ESP32
Hand Gesture Controlled IoT Buzzer using ESP32
A mini IoT project combining computer vision, hand gesture recognition, and ESP32-based IoT control.

The system uses a webcam to detect hand gestures with MediaPipe and OpenCV. Based on the detected hand state, a Python program communicates with an ESP32 over Wi-Fi and remotely controls a buzzer.

How It Works
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Landmark Detection
   ↓
Finger Detection
   ↓
Hand Open / Hand Closed
   ↓
HTTP Request over Wi-Fi
   ↓
ESP32
   ↓
Buzzer ON / OFF
Gesture Logic
Hand Closed → Buzzer ON
Hand Open → Buzzer OFF
No Hand Detected → No buzzer command is sent
The Python program counts the raised fingers using hand landmark coordinates. It sends a command to the ESP32 only when the detected hand status changes.

Technologies Used
ESP32
Arduino
Python
OpenCV
MediaPipe
HTTP
Wi-Fi
Computer Vision
Main Components
Python Application
The Python application:

Captures video from the webcam.
Flips and converts the camera frame to RGB.
Uses MediaPipe's hand-landmark detector.
Checks finger positions to estimate the number of raised fingers.
Classifies the hand as OPEN or CLOSED.
Sends an HTTP request to the ESP32 to control the buzzer.
ESP32
The ESP32 receives HTTP requests from the Python application and provides endpoints for:

/buzzer/on
/buzzer/off
These endpoints are used to switch the buzzer on or off.

Project Features
Real-time hand gesture detection
Finger counting
Wi-Fi-based communication between computer and ESP32
Remote buzzer control
Computer vision integrated with an IoT device
Command transmission only when gesture status changes
What I Learned
This project helped me understand how computer vision can be integrated with IoT hardware. I also gained practical experience with ESP32 networking, HTTP communication, webcam-based hand tracking, and connecting a Python application with an embedded device.

Future Improvements
Add more gestures for controlling multiple devices
Control LEDs, relays, or other actuators
Improve gesture classification using more robust hand features
Add a web-based monitoring interface
Support multiple ESP32 devices
