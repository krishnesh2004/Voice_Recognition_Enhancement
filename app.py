from flask import Flask, render_template, request
import speech_recognition as sr
import noisereduce as nr
import numpy as np
import scipy.io.wavfile as wav
import os
from pydub import AudioSegment

# Force FFmpeg path
AudioSegment.converter = os.path.join(os.getcwd(), "ffmpeg.exe")
print(f"[DEBUG] Using FFmpeg at: {AudioSegment.converter}")

app = Flask(__name__)

UPLOAD_FOLDER = 'samples'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    print("[DEBUG] Entered index() route")
    transcription = ""

    if request.method == 'POST':
        print("[DEBUG] Received POST request")

        if 'audiofile' in request.files:
            file = request.files['audiofile']
            print(f"[DEBUG] Got file: {file.filename}")

            # Save original file
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            print(f"[DEBUG] Saved uploaded file to: {filepath}")

            # Convert to WAV using pydub
            wav_path = os.path.splitext(filepath)[0] + "_converted.wav"
            try:
                audio = AudioSegment.from_file(filepath)
                audio.export(wav_path, format="wav")
                print(f"[DEBUG] Converted audio to: {wav_path}")
            except Exception as e:
                print(f"[ERROR] Could not convert audio: {e}")
                transcription = "Error: Could not convert audio. Check ffmpeg."
                return render_template("index.html", transcription=transcription)

            # Noise reduction
            try:
                rate, data = wav.read(wav_path)
                reduced_noise = nr.reduce_noise(y=data, sr=rate)
                wav.write(wav_path, rate, reduced_noise)
                print(f"[DEBUG] Noise reduction applied and saved to: {wav_path}")
            except Exception as e:
                print(f"[ERROR] Noise reduction failed: {e}")
                transcription = "Error: Noise reduction failed."
                return render_template("index.html", transcription=transcription)

            # Speech recognition
            recognizer = sr.Recognizer()
            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
                try:
                    transcription = recognizer.recognize_google(audio_data)
                    print(f"[DEBUG] Transcription: {transcription}")
                except sr.UnknownValueError:
                    transcription = "Could not understand audio"
                except sr.RequestError as e:
                    transcription = f"Could not request results; {e}"

        else:
            print("[DEBUG] No file found in request.files")
            transcription = "Error: No file uploaded."

    return render_template("index.html", transcription=transcription)

if __name__ == '__main__':
    print("[DEBUG] Starting Flask app...")
    app.run(debug=True)
