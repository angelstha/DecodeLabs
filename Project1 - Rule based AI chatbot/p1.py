import re
import random

print("=" * 50)
print("      Welcome to the Rule-Based AI Chatbot")
print("=" * 50)
print("Type 'bye' anytime to exit.\n")

# Responses with multiple options for variety
responses = {
    "hello": ["Hello! Nice to meet you.", "Hi there!", "Hey! How’s it going?"],
    "how are you": ["I'm just a chatbot, but I'm doing great!", "Feeling awesome, thanks for asking!"],
    "what is your name": ["My name is DecodeBot.", "You can call me DecodeBot."],
    "who created you": ["I was created as a Rule-Based AI Chatbot using Python."],
    "what is ai": ["Artificial Intelligence is the ability of computers to perform tasks that normally require human intelligence."],
    "what can you do": ["I can answer simple predefined questions and have basic conversations."],
    "thank you": ["You're welcome!", "Happy to help!"],
    "good morning": ["Good Morning! Have a wonderful day!"],
    "good afternoon": ["Good Afternoon!"],
    "good evening": ["Good Evening!"],
    "good night": ["Good Night! Sleep well."],
    "help": [
        "You can ask me things like:\n"
        "- hello\n"
        "- how are you\n"
        "- what is your name\n"
        "- what is ai\n"
        "- who created you\n"
        "- what can you do\n"
        "- bye"
    ]
}

def get_response(user_input):
    # Regex patterns for flexible matching
    patterns = {
        r"(hello|hi|hey)": "hello",
        r"(thank you|thanks)": "thank you",
        r"how are you": "how are you",
        r"what is your name": "what is your name",
        r"who created you": "who created you",
        r"what is ai": "what is ai",
        r"what can you do": "what can you do",
        r"good morning": "good morning",
        r"good afternoon": "good afternoon",
        r"good evening": "good evening",
        r"good night": "good night",
        r"help": "help"
    }
    for pattern, key in patterns.items():
        if re.search(pattern, user_input):
            return random.choice(responses[key])
    return None

# Chat loop
while True:
    user_input = input("\nYou : ").strip().lower()
    if user_input == "bye":
        print("\nBot : Goodbye! Have a wonderful day.")
        break
    elif user_input == "":
        print("Bot : Please type something.")
        continue
    response = get_response(user_input)
    if response:
        print("Bot :", response)
    else:
        print("Bot : Sorry, I don't understand that.")
        print("Bot : Type 'help' to see what you can ask.")

print("\nProgram Ended.")
