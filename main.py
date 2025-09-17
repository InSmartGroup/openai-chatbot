import ask_chatbot
from save_load_chat_history import save_chat, load_chat

if __name__ == "__main__":
    messages = load_chat()

    while True:
        user_input = input("Ask ChatGPT:\n")
        if user_input == "quit".lower():
            save_chat(messages)
            break

        chat_response = ask_chatbot.ask(user_input, messages)
        print("".center(50, "-"))
        print(f"{chat_response}")
        print("".center(50, "-"))
