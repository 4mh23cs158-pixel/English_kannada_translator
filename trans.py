# English to Kannada Translator with Speech
# Works on Python 3.13 (NO cgi, NO googletrans)

from deep_translator import GoogleTranslator
from gtts import gTTS
import os

def english_to_kannada_with_speech():
    text = input("Enter English text: ").strip()

    if not text:
        print("No input provided.")
        return

    # Translate English -> Kannada
    kannada_text = GoogleTranslator(source='en', target='kn').translate(text)

    print("\nEnglish:")
    print(text)

    print("\nKannada:")
    print(kannada_text)

    # Convert Kannada text to speech
    audio_file = "kannada_audio.mp3"
    tts = gTTS(text=kannada_text, lang='kn')
    tts.save(audio_file)

    print("\nKannada audio saved as:", audio_file)

    # Open audio automatically (Windows)
    os.startfile(audio_file)

if __name__ == "__main__":
    english_to_kannada_with_speech()
