def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # Define some basic rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input or "what's up" in user_input:
        return "I'm just a chat bot, so I don't have feelings, but thanks for asking!"
    elif "what's your name" in user_input:
        return "I'm a chat bot. You can call me Bot."
    elif "weather" in user_input:
         return "I'm sorry, I don't have access to real-time data for weather."
    elif "time" in user_input:
        return "I'm sorry, I don't have access to real-time."
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Chat bot: Hello! I'm your simple rule-based chat bot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chat bot: Goodbye! Have a great day!")
            break
        response = get_bot_response(user_input)
        print("Chat bot:", response)

if __name__ == "__main__":
    main()
