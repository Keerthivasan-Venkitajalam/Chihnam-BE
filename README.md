# Chihnam Backend

Chihnam is an AI-powered real-time sign language translator. This backend provides Speech-to-Text (ASR) and Text-to-Speech (TTS) functionalities.

## 📌 Features
- 🎙️ **Speech Recognition** using OpenAI Whisper and Wav2Vec2
- 🔊 **Text-to-Speech** using Google TTS and Coqui TTS
- 🖼️ **Spectrogram Generation** for audio visualization
- 📂 **File Upload API** for audio processing
- 🌍 **Accessible via ngrok** for remote integration

## 🚀 Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/signbridge-backend.git
   cd signbridge-backend
   ```

2. **Create a virtual environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up ngrok**  
   Replace `NGROK_AUTH_TOKEN` in `config.py` with your actual token.

5. **Run the server**
   ```sh
   python run.py
   ```

6. **Access the API**  
   The public URL (provided by ngrok) will be displayed in the terminal.

## 📡 API Endpoints

### 🎙️ Speech-to-Text (ASR)
- **`POST /upload-audio`**  
  Upload an audio file for transcription.

### 🔊 Text-to-Speech (TTS)
- **`POST /text-to-speech`**  
  Convert text into speech using Google TTS or Coqui TTS.

### 🖼️ Spectrogram Visualization
- **`GET /get-spectrogram`**  
  Retrieve the generated spectrogram.

## 🛠️ Directory Structure

```
signbridge-backend/
│── app/
│   │── __init__.py
│   │── routes.py         # API routes (ASR, TTS, etc.)
│   │── processing.py     # Audio processing functions
│   │── tts.py           # Text-to-Speech functions
│   │── asr.py           # Speech-to-Text (Whisper, Wav2Vec2)
│   │── utils.py         # Utility functions (file handling, logging)
│── models/
│   │── whisper/         # Whisper model files (if needed)
│   │── tts/             # Coqui TTS models (optional)
│── static/
│   │── spectrograms/    # Spectrogram images
│── uploads/
│   │── audio/           # Uploaded audio files
│── config.py           # Configuration settings
│── run.py              # Flask entry point
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

## 💡 Future Enhancements
- Add real-time streaming ASR
- Improve denoising techniques
- Implement multilingual support

---
