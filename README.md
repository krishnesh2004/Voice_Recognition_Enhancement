# Voice Recognition Enhancement 🎙️

This project is a **Voice Recognition Enhancement Tool** built with **Python & Flask**, which:

- 🎧 Accepts uploaded audio files (MP3, WAV, OPUS, etc.)
- 🔄 Converts them to WAV format using `pydub` & `ffmpeg`
- 🚿 Applies noise reduction using `noisereduce`
- 📝 Transcribes the cleaned audio into text using `SpeechRecognition` (Google API).

---

## 🚀 Features
- Upload any common audio format (MP3, WAV, OPUS, etc.)
- Automatic format conversion to WAV via `ffmpeg`
- Noise reduction to improve transcription accuracy
- Converts speech to text with Google Speech Recognition
- Minimal web interface built with Flask + HTML/CSS

---

## 📸 Demo

**Before uploading an audio file:**  
<br>
<img src="https://github.com/user-attachments/assets/83fc6612-4a65-4244-8cf2-b6c39f7e0d03" width="500"/>
<br><br>

**After uploading and processing an audio file:**  
<br>
<img src="https://github.com/user-attachments/assets/3d6c86e8-228e-4385-8a8f-e51f842fbb44" width="500"/>
<br>

---

## 🛠️ Tech Stack
- **Backend (Python):**
  - Flask
  - SpeechRecognition
  - pydub
  - noisereduce
  - numpy, scipy
- **Frontend:**
  - HTML / CSS

---
