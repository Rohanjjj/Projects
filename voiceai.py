import speech_recognition as sr
import pyttsx3
import openai
import requests
import webbrowser
import datetime
import time

# Initialize the speech engine and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Set up OpenAI API key
openai.api_key = ""  # Replace with your OpenAI API key
def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a user's command."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Could you please repeat?")
            return ""
        except sr.RequestError as e:
            speak("Sorry, I'm unable to process your request at the moment.")
            return ""

def get_ai_response(prompt):
    """Get a response from OpenAI's GPT."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I'm unable to process your request at the moment."

def perform_task(command):
    """Perform tasks based on the command."""
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {current_time}")

    elif 'open website' in command:
        speak("Which website would you like to open?")
        website = listen()
        if website:
            url = f"https://{website}"
            webbrowser.open(url)
            speak(f"Opening {website}")

    elif 'search' in command:
        speak("What would you like to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Searching for {query}")

    elif 'weather' in command:
        api_key = ""  # Replace with your weather API key
        speak("Which city's weather would you like to know?")
        city = listen()
        if city:
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(weather_url).json()
            if response.get("main"):
                temperature = response['main']['temp']
                weather_description = response['weather'][0]['description']
                speak(f"The weather in {city} is {weather_description} with a temperature of {temperature} degrees Celsius.")
            else:
                speak("Sorry, I couldn't find the weather for that city.")

    elif 'your name' in command:
        speak("I am your personal AI assistant.")

    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        exit()

    else:
        ai_response = get_ai_response(command)
        speak(ai_response)

# Main loop to continuously listen for commands
if __name__ == "__main__":
    speak("Hello! I am your personal assistant. How can I help you today?")
    while True:
        user_command = listen()
        if user_command:
            perform_task(user_command)
