import json


def save_chat(messages):
    with open("chat_log.json", "w", encoding="utf-8") as file:
        json.dump(messages, file, ensure_ascii=False, indent=2)


def load_chat():
    try:
        with open("chat_log.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {
            "role": "system",
            "content": "You are a helpful assistant who always provides meaningful and detailed responses."
        }
