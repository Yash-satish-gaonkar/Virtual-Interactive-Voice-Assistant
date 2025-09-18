import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize speech recognizer
recognizer = sr.Recognizer()

def speak(message):
    """Speaks the provided message."""
    engine.say(message)
    engine.runAndWait()

def cmd():
    """Listens for a command and executes it."""
    with sr.Microphone() as source:
        print("Clearing background noises... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Listening...')
        try:
            recordedaudio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(recordedaudio, language='en_US').lower()
            print(f'You said: {text}')
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")
            speak("Sorry, I didn't catch that. Could you repeat?")
            return
        except sr.RequestError:
            print("Could not connect to the recognition service.")
            speak("Could not connect to the recognition service.")
            return
        except Exception as ex:
            print(f"An error occurred: {ex}")
            speak("An error occurred.")
            return

        # Process commands
        if 'chrome' in text:
            speak('Opening Chrome...')
            try:
                #subprocess.Popen(["chrome"])  # Cross-platform approach
                subprocess.Popen(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", shell=True)
            except FileNotFoundError:
                speak("Chrome is not installed or not in your PATH.")

        elif 'search' in text:
            query = text.replace('search', '').strip()
            #print(query)
            if query:
                speak(f'searching {query} on google...')
                pywhatkit.search(query)
            else:
                speak("Please specify what you want me to search.")

        elif 'time' in text:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            print(f'The time is {current_time}')
            speak(f'The time is {current_time}')
        elif 'play' in text:
            query = text.replace('play', '').strip()
            if query:
                speak(f'Playing {query} on YouTube...')
                pywhatkit.playonyt(query)
            else:
                speak("Please specify what you want me to play.")
        elif 'youtube' in text:
            speak('Opening YouTube...')
            webbrowser.open('https://www.youtube.com')

        elif "your name" in text:
            speak("Myself Viva.")

        elif 'exit' in text or 'quit' in text:
            speak('Goodbye!')
            sys.exit()
        else:
            speak("I didn't understand that command. Please try again.")

# Main loop
if __name__ == "__main__":
    speak("Hello!Iam Virtual Interactive Voice Assistant. Simply VIVA. How can I assist you today?")
    while True:
        cmd()
