import requests
import webbrowser
import datetime
import time
import os
import wikipedia
import pyjokes
import random

def get_ai_response(prompt):
    """Get a response from OpenAI's GPT."""
    api_key = ""  # Replace with your OpenAI API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post("https://api.openai.com/v1/engines/text-davinci-003/completions", headers=headers, json=data)
    return response.json()["choices"][0]["text"].strip()

def perform_task(command):
    """Perform tasks based on the command."""
    if command == "time":
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(f"The current time is {current_time}")

    elif command.startswith("open website"):
        website = command.split(" ")[2]
        url = f"https://{website}" 
        webbrowser.open(url)
        print(f"Opening {website}")

    elif command.startswith("search"):
        query = command.split(" ")[1]
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        print(f"Searching for {query}")

    elif command.startswith("weather"):
        api_key = ""  # Replace with your weather API key
        city = command.split(" ")[1]
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(weather_url).json()
        if response.get("main"):
            temperature = response['main']['temp']
            weather_description = response['weather'][0]['description']
            print(f"The weather in {city} is {weather_description} with a temperature of {temperature} degrees Celsius.")
        else:
            print("Sorry, I couldn't find the weather for that city.")

    elif command == "Rohan":
        print("I am your personal AI assistant.")

    elif command == "exit" or command == "quit":
        print("Goodbye!")
        exit()

    elif command == "tell me a joke":
        joke = pyjokes.get_joke()
        print(joke)

    elif command.startswith("play music"):
        music = command.split(" ")[2]
        url = f"https://www.youtube.com/results?search_query={music}"
        webbrowser.open(url)
        print(f"Playing {music}")

    elif command.startswith("open file"):
        file_name = command.split(" ")[2]
        try:
            os.startfile(file_name)
            print(f"Opening {file_name}")
        except Exception as e:
            print("Sorry, I couldn't find that file.")

    elif command.startswith("wikipedia"):
        topic = command.split(" ")[1]
        try:
            result = wikipedia.summary(topic, sentences=2)
            print(result)
        except Exception as e:
            print("Sorry, I couldn't find any information about that topic.")

    elif command == "random fact":
        fact = random.choice(["The shortest war in history was between Britain and Zanzibar on August 27, 1896, and lasted only 38 minutes.",
                             "The longest word in the English language, according to the Oxford English Dictionary, is pneumonoultramicroscopicsilicovolcanoconiosis, a lung disease caused by inhaling very fine particles"])
        print(fact)

    else:
        ai_response = get_ai_response(command)
        print(ai_response)

def main():
    print("Hello! I am your personal AI assistant. How can I help you today?")
    while True:
        command = input("Enter a command: ")
        perform_task(command)

if __name__ == "__main__":
    main()
