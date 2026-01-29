from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.json
        english_text = data.get("text", "").strip()
        
        if not english_text:
            return jsonify({"error": "No text provided"}), 400
        
        # Translate English to Kannada
        kannada_text = GoogleTranslator(source='en', target='kn').translate(english_text)
        
        return jsonify({
            "english": english_text,
            "kannada": kannada_text
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/speak", methods=["POST"])
def speak():
    try:
        data = request.json
        kannada_text = data.get("text", "").strip()
        
        if not kannada_text:
            return jsonify({"error": "No text provided"}), 400
        
        # Generate speech
        audio_file = "static/kannada_audio.mp3"
        os.makedirs("static", exist_ok=True)
        
        tts = gTTS(text=kannada_text, lang='kn')
        tts.save(audio_file)
        
        return jsonify({
            "audio_url": "/" + audio_file,
            "message": "Audio generated successfully"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)