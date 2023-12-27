import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def personal_assistant():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if command:
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "goodbye" in command or "exit" in command:
                speak("Goodbye! Have a great day.")
                break
            else:
                speak("Sorry, I didn't understand that command. Can you please repeat?")
        else:
            speak("I'm sorry, I couldn't hear you. Can you please repeat?")

if __name__ == "__main__":
    personal_assistant()
