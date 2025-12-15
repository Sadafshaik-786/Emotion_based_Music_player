#  Emotion-Based Music Player using AI

##  Project Description
The Emotion-Based Music Player is an AI-powered application that detects human emotions in real time using a webcam and automatically plays music based on the detected emotion. The system integrates Computer Vision and Deep Learning techniques to analyze facial expressions and deliver a personalized music experience. It uses a pre-trained CNN model through DeepFace for emotion recognition and OpenCV for real-time face detection.

---

##  Key Features
- Real-time face detection using OpenCV  
- Emotion recognition using a pre-trained CNN model (DeepFace)  
- Supports emotions: Happy, Sad, Angry, Fear, Disgust, Surprise, Neutral  
- Automatic emotion-based music recommendation  
- Voice feedback announcing detected emotion  
- Simple and interactive GUI using Tkinter  

---

##  Technologies Used
- **Python**
- **OpenCV** – Camera access and face detection  
- **DeepFace** – Pre-trained CNN for emotion recognition  
- **TensorFlow** – Deep learning backend  
- **Pygame** – Music playback  
- **Tkinter** – Graphical User Interface  
- **pyttsx3** – Text-to-Speech  

---

##  Project Structure


Emotion_based_Music_player/
│── emotion.py
│── README.md
│── music_folder/
│ ├── happy/
│ ├── sad/
│ ├── anger/
│ ├── fear/
│ ├── disgust/
│ ├── surprise/
│ └── neutral/



---

##  Installation Guide

###  Step 1: Install Python
This project requires **Python 3.8 (64-bit)**.

Download Python 3.8.10 from the official site:  
https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe

✔ During installation, check **"Add Python to PATH"**  
✔ Select **"Install for all users"**

---

###  Step 2: Create Virtual Environment (Recommended)

python -m venv faceenv
faceenv\Scripts\activate


---

###  Step 3: Install Required Libraries


pip install opencv-python
pip install deepface
pip install tensorflow==2.9.1
pip install pygame
pip install pyttsx3
pip install numpy==1.23.5



---

##  How to Run the Project

1. Activate the virtual environment:
faceenv\Scripts\activate


2. Run the application:
python emotion.py


3. Click **Start Emotion Detection** in the GUI.
4. Press **Q** to stop camera detection.
5. The system will announce the detected emotion and play emotion-based music.

---

##  Workflow Overview

User Clicks Start
↓
Webcam Captures Face (OpenCV)
↓
Face Detection (Haar Cascade)
↓
Face Cropping (ROI)
↓
CNN Emotion Analysis (DeepFace)
↓
Dominant Emotion Identified
↓
Emotion Displayed on Screen
↓
Emotion Spoken (pyttsx3)
↓
Emotion-based Song Selected
↓
Music Played (pygame)


---

##  Applications
- Emotion-aware music recommendation systems  
- Mental health and stress monitoring  
- Smart AI assistants  
- Human-computer interaction systems  
- Gaming and entertainment applications  

---

##  Future Enhancements
- Continuous emotion tracking  
- Emotion analytics dashboard  
- Mobile and web application version  
- Voice emotion detection  
- AI-generated music based on emotions  

---

##  Author
**Naseem Sadaf Shaik**  
GitHub: https://github.com/Sadafshaik-786

---

##  License
This project is open-source and available under the **MIT License**.


