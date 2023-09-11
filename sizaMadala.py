import pyttsx3
import time
import datetime
import speech_recognition as sr

# Function to use text-to-speech for communication
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to listen for user responses using speech recognition
def listen_for_response():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        speak("Please say 'yes' or 'no'.")
        print("Listening for response...")
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio).strip().lower()
        return response
    except sr.UnknownValueError:
        return "unknown"
    except sr.RequestError:
        return "unknown"

# Define a list of daily routines
daily_routines = [
    "Take your morning medication.",
    "Have a balanced meal for lunch.",
    "Take a short walk in the afternoon.",
    "Enjoy a nutritious dinner.",
    "Remember to get a good night's sleep.",
]

# Greet the user and provide an introductory message
speak("Hello! I'm here to help you with your daily routines.")
speak("It's important to stay healthy and follow your daily routines.")

# Main loop for reminders and user interaction
for task in daily_routines:
    # Remind the user about the current task
    speak(f"Now, it's time for you to {task}")

    # Prompt the user with a yes/no question and listen for their response
    speak("Have you completed this task? (yes/no)")
    while True:
        response = listen_for_response()
        if response == "yes":
            speak("Great job! Keep it up.")
            break
        elif response == "no":
            speak("No worries, please complete the task when you can.")
            speak("I'll check up on you after 30 minutes because it's my duty to make sure you stay healthy.")
            time.sleep(1800)  # Wait for 30 minutes (1800 seconds) before reminding again
            break
        elif response == "unknown":
            speak("Please say 'yes' or 'no', or if you need assistance, just ask.")
        else:
            speak("Sorry, I didn't understand your response. Please say 'yes' or 'no'.")

    # Ask the user to say something if there's a period of silence
    while response == "unknown":
        speak("Please say something. I'm here to help you.")
        response = listen_for_response()

# Final message
speak("You've completed all your daily routines. Well done!")
