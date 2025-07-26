import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Press Enter and then speak clearly into your microphone...")
    input()  # Wait for user to press Enter
    print("Listening...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    print("Recognizing...")
    try:
        text = recognizer.recognize_google(audio)
        print("You said: ", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    main()
