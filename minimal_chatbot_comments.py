from openai import OpenAI  
import os 

# Initialize the OpenAI client using the API key from an environment variable.
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# Alternatively, you can uncomment the next line and replace "your-actual-key-here" with your OpenAI API key.
# client = OpenAI(api_key="sk-your-actual-key-here")

# Function to load the content of a document .
def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to generate a chatbot response based on the user input and document content.
def chatbot_response(user_input, document_content):
    # Create a response using OpenAI's chat completion API.
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Specify the model to use.
        messages=[
            # System message to instruct the chatbot to only answer questions with the provided document content.
            {"role": "system", "content": "Only answer questions with this document content: " + document_content},
            # User message containing the user's input.
            {"role": "user", "content": user_input}
        ]
    )
    # Return the chatbot's response.
    return response.choices[0].message.content

# Main function to run the chatbot.
def main():
    # Load the content of the document.
    document_content = load_document("yourdoc.txt")
    # Print a welcome message.
    print("Hi, my name is Alfred and I'm our AI assistant! What can I help you with?")
    while True:
        # Get the user's input.
        user_input = input("\nDu: ")
        # If the user types "exit", end the conversation.
        if user_input.lower() == "exit":
            print("Alfred: Thanks for chatting with me! Goodbye!")
            break
        # Generate a response from the chatbot.
        response = chatbot_response(user_input, document_content)
        # Print the chatbot's response.
        print("Alfred:", response)

if __name__ == "__main__":
    main()

