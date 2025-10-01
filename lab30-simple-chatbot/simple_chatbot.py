#!/usr/bin/env python3
# Lab 30: Simple Chatbot Logic

def simple_chatbot(user_input):
    if user_input.lower() == "hello":
        return "Hi there! How can I help you today?"
    elif user_input.lower() == "what is your name?":
        return "I am a simple chatbot created for this lab."
    elif user_input.lower() == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

def run_chatbot():
    print("Welcome to the Simple Chatbot! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        response = simple_chatbot(user_input)
        print("Bot: " + response)
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    run_chatbot()
