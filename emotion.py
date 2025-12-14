import cv2
from deepface import DeepFace
import random
import pygame
import tkinter as tk
import pyttsx3

# Initialize Pygame for music playback
pygame.init()

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# -------------------- UPDATED MUSIC PATHS --------------------

BASE_PATH = r"C:\MY_Projects\face\music_pro"

HAPPY = [
    rf"{BASE_PATH}\happy\1.mp3", rf"{BASE_PATH}\happy\2.mp3", rf"{BASE_PATH}\happy\3.mp3",
    rf"{BASE_PATH}\happy\4.mp3", rf"{BASE_PATH}\happy\5.mp3", rf"{BASE_PATH}\happy\6.mp3",
    rf"{BASE_PATH}\happy\7.mp3", rf"{BASE_PATH}\happy\8.mp3", rf"{BASE_PATH}\happy\9.mp3",
    rf"{BASE_PATH}\happy\10.mp3", rf"{BASE_PATH}\happy\11.mp3", rf"{BASE_PATH}\happy\12.mp3",
    rf"{BASE_PATH}\happy\13.mp3", rf"{BASE_PATH}\happy\14.mp3", rf"{BASE_PATH}\happy\15.mp3",
    rf"{BASE_PATH}\happy\16.mp3", rf"{BASE_PATH}\happy\17.mp3", rf"{BASE_PATH}\happy\18.mp3"
]

FEAR = [
    rf"{BASE_PATH}\fear\1.mp3", rf"{BASE_PATH}\fear\2.mp3", rf"{BASE_PATH}\fear\3.mp3",
    rf"{BASE_PATH}\fear\4.mp3", rf"{BASE_PATH}\fear\5.mp3", rf"{BASE_PATH}\fear\6.mp3",
    rf"{BASE_PATH}\fear\7.mp3", rf"{BASE_PATH}\fear\8.mp3", rf"{BASE_PATH}\fear\9.mp3",
    rf"{BASE_PATH}\fear\10.mp3", rf"{BASE_PATH}\fear\11.mp3", rf"{BASE_PATH}\fear\12.mp3",
    rf"{BASE_PATH}\fear\13.mp3", rf"{BASE_PATH}\fear\14.mp3"
]

SAD = [
    rf"{BASE_PATH}\sad\1.mp3", rf"{BASE_PATH}\sad\2.mp3", rf"{BASE_PATH}\sad\3.mp3",
    rf"{BASE_PATH}\sad\4.mp3", rf"{BASE_PATH}\sad\5.mp3", rf"{BASE_PATH}\sad\6.mp3",
    rf"{BASE_PATH}\sad\7.mp3", rf"{BASE_PATH}\sad\8.mp3", rf"{BASE_PATH}\sad\9.mp3",
    rf"{BASE_PATH}\sad\10.mp3", rf"{BASE_PATH}\sad\11.mp3", rf"{BASE_PATH}\sad\12.mp3",
    rf"{BASE_PATH}\sad\13.mp3", rf"{BASE_PATH}\sad\14.mp3", rf"{BASE_PATH}\sad\15.mp3"
]

ANGRY = [
    rf"{BASE_PATH}\anger\1.mp3", rf"{BASE_PATH}\anger\2.mp3", rf"{BASE_PATH}\anger\3.mp3",
    rf"{BASE_PATH}\anger\4.mp3", rf"{BASE_PATH}\anger\5.mp3", rf"{BASE_PATH}\anger\6.mp3",
    rf"{BASE_PATH}\anger\7.mp3", rf"{BASE_PATH}\anger\8.mp3", rf"{BASE_PATH}\anger\9.mp3",
    rf"{BASE_PATH}\anger\10.mp3"
]

DISGUST = [
    rf"{BASE_PATH}\disgust\1.mp3", rf"{BASE_PATH}\disgust\2.mp3", rf"{BASE_PATH}\disgust\3.mp3",
    rf"{BASE_PATH}\disgust\4.mp3", rf"{BASE_PATH}\disgust\5.mp3", rf"{BASE_PATH}\disgust\6.mp3"
]

SURPRISE = [
    rf"{BASE_PATH}\surprise\1.mp3", rf"{BASE_PATH}\surprise\2.mp3", rf"{BASE_PATH}\surprise\3.mp3"
]

NEUTRAL = [
    rf"{BASE_PATH}\neutral\1.mp3", rf"{BASE_PATH}\neutral\2.mp3", rf"{BASE_PATH}\neutral\3.mp3",
    rf"{BASE_PATH}\neutral\4.mp3", rf"{BASE_PATH}\neutral\5.mp3", rf"{BASE_PATH}\neutral\6.mp3",
    rf"{BASE_PATH}\neutral\7.mp3", rf"{BASE_PATH}\neutral\8.mp3", rf"{BASE_PATH}\neutral\9.mp3",
    rf"{BASE_PATH}\neutral\10.mp3", rf"{BASE_PATH}\neutral\11.mp3"
]

# -------------------------------------------------------------

# Function to detect emotions
def detect_emotion():
    cap = cv2.VideoCapture(0)
    emotion = None

    while True:
        ret, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_roi = rgb_frame[y:y + h, x:x + w]

            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, f"Emotion: {emotion}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow('Real-time Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    speak_emotion(emotion)
    play_music(emotion)

# Speak detected emotion
def speak_emotion(emotion):
    engine.say(f"The detected emotion is {emotion}")
    engine.runAndWait()

# Play music
def play_music(emotion):
    emotions_music = {
        "happy": HAPPY,
        "fear": FEAR,
        "sad": SAD,
        "angry": ANGRY,
        "disgust": DISGUST,
        "surprise": SURPRISE,
        "neutral": NEUTRAL
    }

    if emotion in emotions_music:
        random_song = random.choice(emotions_music[emotion])
        pygame.mixer.music.load(random_song)
        pygame.mixer.music.play()

# Stop music
def stop_music():
    pygame.mixer.music.stop()

# GUI Window
root = tk.Tk()
root.title("Emotion Detection and Music Player")
root.geometry("500x200")

start_detection_btn = tk.Button(root, text="Start Emotion Detection", command=detect_emotion)
start_detection_btn.pack(pady=10)

stop_music_btn = tk.Button(root, text="Stop Music", command=stop_music)
stop_music_btn.pack(pady=10)

root.mainloop()
