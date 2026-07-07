"""
Project1: Rule-Based AI Chatbot
DecodeLabs Internship
Made by: Kashmala Rizwan
A chatbot that matches user input against predefined rules and responds
accordingly. Runs continuously until the user exits.

Extra features added on top of the base version:
- Remembers the user's name and personalizes replies with it
- An explicit if-elif command ("time") alongside the dictionary lookup
"""

from datetime import datetime

# 1.Knowledge base

# Using "in" checks below instead of an exact dict lookup lets the bot
# catch a keyword anywhere in a longer sentence, not just an exact match.

responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm running perfectly! How about you?",
    "what is your name": "I'm ChatBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you based on a few predefined rules and commands.",
    "help": "Try greeting me, telling me your name, asking 'time', or say 'bye' to exit.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}
# words to end conversation
exit_commands = {"bye", "exit", "quit"}

# 2: Matchinng Function
def extract_name(clean_input: str) -> str | None:
    """Looks for patterns like 'my name is X' or 'i am X' and pulls out X."""
    for phrase in ("my name is ", "i am ", "i'm "):
        if phrase in clean_input:
            return clean_input.split(phrase, 1)[1].strip().title()
    return None


def get_response(clean_input: str, user_name: str | None) -> str:
    """
    Checks the cleaned input for one special command first (if-elif),
    then falls back to the dictionary-based knowledge base, then a
    final fallback message.
    """

    if clean_input == "time":
        return f"It's currently {datetime.now().strftime('%H:%M')}."
he
    for keyword, reply in responses.items():
        if keyword in clean_input:
            return reply if not user_name else reply.replace("!", f", {user_name}!", 1)

    return "I do not understand. Type 'help' for options."

# 3: Main chat Loop
def run_chatbot():
    """Main chat loop: keeps taking input until the user chooses to exit."""
    user_name = None
    print("ChatBot: Hello! I'm your rule-based assistant. Type 'bye' to exit.")

    while True:
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()

        if clean_input in exit_commands:
            farewell = f"Goodbye, {user_name}!" if user_name else "Goodbye! Have a great day."
            print(f"ChatBot: {farewell}")
            break

        if clean_input == "":
            print("ChatBot: I didn't catch that — try typing something!")
            continue

        found_name = extract_name(clean_input)
        if found_name:
            user_name = found_name
            print(f"ChatBot: Nice to meet you, {user_name}!")
            continue

        reply = get_response(clean_input, user_name)
        print(f"ChatBot: {reply}")

# 4: Run the program

if __name__ == "__main__":
    run_chatbot()
