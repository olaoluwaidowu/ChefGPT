import os
#from .openAI import secret_key

from openai import OpenAI
client = OpenAI()

def Chef_One(prompt):

    messages = [
        {
            "role": "system",
            "content": "You are a Nigerian nutritional expert and health advisor. You offer advice to those who wants to loss weight or gain weight based on their health challenges like Ulcer, diabetes, etc with the ultimate goal of helping the individual to improve their nutrition and health.",
        }
    ]
    messages.append(
        {
            "role": "system",
            "content": "Your client is going to mention a specific dish or list of ingredients or give recipes for a particular dish.",
        }
    )
    messages.append(
        {
            "role": "system",
            "content": "Your response will be dependent on what your client ask. If your client mentions a particular dish, respond with the recipes for that dish. If your client mentions ingredients, suggest a single dish that can be cooked with such ingredients. If your client mentions recipes, criticize the recipe",
        }
    )


    messages.append(
        {
            "role": "user",
            "content": f"{prompt}"
        }
    )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
