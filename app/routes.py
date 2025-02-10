from flask import Blueprint, request, jsonify, send_file
from app.asr import transcribe_audio
from app.tts import synthesize_speech
from app.utils import save_uploaded_file

routes = Blueprint('routes', __name__)

@routes.route('/upload-audio', methods=['POST'])
def upload_audio():
    """Receives an audio file, processes it, and returns the transcription"""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = save_uploaded_file(file)

    # Transcribe the audio
    transcription = transcribe_audio(file_path)

    return jsonify({"transcription": transcription})

@routes.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    """Receives text and converts it to speech"""
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data['text']
    tts_file = synthesize_speech(text)

    return send_file(tts_file, as_attachment=True, mimetype="audio/wav")

@routes.route('/get-spectrogram', methods=['GET'])
def get_spectrogram():
    """Returns the spectrogram image of the last processed audio"""
    return send_file("static/spectrograms/latest_spectrogram.png", mimetype='image/png')
