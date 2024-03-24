from ChefGPT import Chef_One
import os
#from ../openAI/Secret_Key import secret_key

from openai import OpenAI
client = OpenAI()

messages = [
     {
          "role": "system",
          "content": "You are a waiter.",
     }
]
messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe about a specific dish, or ingredients for a specific dish, or recipes for a specific dish. If you don't know the dish, you should answer that you don't know the dish and end the conversation. If the client does not ask for things related to the above, you should specify what the questions should center on and end the conversation",
     }
)

messages.append(
     {
          "role": "system",
          "content": "If client ask for options related to Ghanian dish, respond with 1, if client ask for an italian dish respond with 2, if client ask for a Nigerian dish respond with 3. If the client does not ask for things related to the above, you should specify that your chefs deal with Nigerian, Ghanian and italian food recipes and the conversation",
     }
)

while True:
    dish = input("\n\nPlease input the name of the dish you want a recipe for \nor specify ingredients to find a corresponding dish,\nor recipes you want me to criticize:\n")
    messages.append(
        {
            "role": "user",
            "content": f"{dish}"
        }
    )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

    for chunk in stream:
        
        if chunk.choices[0].delta.content == '1':
            Chef_One(dish)
        elif chunk.choices[0].delta.content == '2':
            Chef_Two(dish)
        elif chunk.choices[0].delta.content == '3':
            Chef_Three(dish)
        else:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            
            

