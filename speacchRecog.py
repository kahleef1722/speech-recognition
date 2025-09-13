import sounddevice as sd
import numpy as np
import wave
import speech_recognition as sr
import os

# File to save
filename = "output.wav"
duration = 5   # seconds
sample_rate = 44100
channels = 2

# 🎙️ Record audio
print("🎙️ Recording...")
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
sd.wait()

print("✅ Recording finished, saving...")

# Save as WAV file
with wave.open(filename, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(recording.tobytes())

print(f"💾 Audio saved as {filename}")

# 🎤 Convert speech to text
recognizer = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)  # uses Google API (free, requires internet)
    print("📝 Recognized Text:")
    print(text)
except sr.UnknownValueError:
    print("❌ Could not understand audio")
except sr.RequestError:
    print("⚠️ Could not request results, check internet connection")
