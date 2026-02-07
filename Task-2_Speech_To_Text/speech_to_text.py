import speech_recognition as sr

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("=== SPEECH TO TEXT TOOL ===")
    audio_file = input("Enter the path of your audio file (.wav): ")

    print("\nTranscribing...")
    result = speech_to_text(audio_file)

    print("\n=== TRANSCRIPTION ===")
    print(result)

if __name__ == "__main__":
    main()
