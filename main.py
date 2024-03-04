import os
import openai
import requests
import json

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a assistant which informs about temperature."},
        {"role": "user", "content": "Hey there"}
    ]
)

# print(completion.choices[0].message)

def get_current_weather(location):
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"

    querystring = {"text": "fishermans wharf", "language": "en"}

    headers = {
        "X-RapidAPI-Key": "9a88c5f33amshda19cd888996b49p1242f5jsn14c79e1c8962",
        "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    # print(type(response))

    return response.json()

response=get_current_weather("Bengaluru")
# print(response)

functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },

            },
            "required": ["location"],
        },
    }
]

user_message = "What is the temperature of Bangalore"
messages=[]
messages.append({"role":"user","content":user_message})
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)
print(completion.choices[0].message)
# print(messages)
# print(completion)
# response= completion.choices[0].message
