import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Function to recognize speech input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google Web Speech API
            query = recognizer.recognize_google(audio).lower()
            print("You said: " + query)
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print("Could not request results; check your network connection.")
            return None

# Main program loop
while True:
    # Listen for user input
    user_input = listen()

    if user_input:
        # Add your custom commands here
        if "hello" in user_input:
            speak("Hello! How can I assist you?")
            break
        elif "bye" in user_input:
            speak("Goodbye! Have a great day!")
            break
        elif"hi" in user_input:
            speak("nuvu gudu ra puka!")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

# Release the resources
engine.stop()
