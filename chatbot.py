print("======================================")
print("      STUDENT ASSISTANCE CHATBOT")
print("======================================")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user_input:
        print("Bot: I am a rule-based student assistance chatbot.")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "python" in user_input:
        print("Bot: Python is a beginner-friendly programming language.")

    elif "internship" in user_input:
        print("Bot: Internships help you gain practical experience and industry skills.")

    elif "study" in user_input or "exam" in user_input:
        print("Bot: Make a study schedule, practice regularly, and revise important topics.")

    elif "help" in user_input:
        print("Bot: I can help with Python, internships, courses, and study tips.")

    elif "thank" in user_input:
        print("Bot: You're welcome! Happy to help.")

    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")