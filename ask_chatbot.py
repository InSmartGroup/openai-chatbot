import requests

from API_KEYS import API_OPENAI

URL = "https://api.openai.com/v1/chat/completions"


def ask(user_input: str, chat_list: list):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_OPENAI}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": chat_list
    }

    chat_list.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:
        response = requests.post(url=URL, headers=headers, json=payload)
        chat_response = response.json()["choices"][0]["message"]["content"]

        chat_list.append(
            {
                "role": "assistant",
                "content": chat_response
            }
        )

        return chat_response

    except KeyError:
        print("An error occurred. Printing the output...")
        print(response.text)
