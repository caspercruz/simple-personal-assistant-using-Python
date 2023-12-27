# simple-personal-assistant-using-Python
Below is an example of a simple personal assistant that recognizes voice input using the SpeechRecognition library and responds to basic commands.
Import Libraries:

python
Copy code
import speech_recognition as sr
import pyttsx3
These lines import the necessary libraries. speech_recognition is used for recognizing speech input, and pyttsx3 is used for text-to-speech synthesis.

Define the speak Function:

python
Copy code
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
This function initializes the text-to-speech engine using pyttsx3 and speaks the given text.

Define the listen Function:

python
Copy code
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
This function uses the speech_recognition library to capture audio from the microphone, sends it to Google's speech recognition service, and returns the recognized text.

Define the personal_assistant Function:

python
Copy code
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
This function initiates the personal assistant. It starts by greeting the user and then enters into a loop where it continuously listens for commands. Based on the recognized commands, it responds appropriately.

Run the Personal Assistant:

python
Copy code
if __name__ == "__main__":
    personal_assistant()
This block checks if the script is being run as the main program, and if so, it calls the personal_assistant function to start the interaction.

When you run this script, the personal assistant will greet you, listen for your commands, and respond accordingly. The main loop continues until you say "goodbye" or "exit," at which point the assistant bids farewell and the script exits.
