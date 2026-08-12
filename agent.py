# Simple AI chatbot agent that can respond to user input.
def respond_to_input(user_input):
    # Basic responses based on user input
    if "hello" in user_input.lower():
        return "Hello! I am Your study assistant. How can I help you today?"
    elif "python" in user_input.lower():
        return "Python is a simple and powerful programming language."
    elif "ai" in user_input.lower():
        return "AI means Artificial Intelligence.It allows computers to perform intelligent tasks."
    elif "machine learning" in user_input.lower():
            return "Machine Learning is a part of AI that learns from data."
    elif "bye" in user_input.lower():
                return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?" 
# Sart the chatbot
def main():
    while True:
        user_input = input("You: ")
        response = respond_to_input(user_input)
        print("Bot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
