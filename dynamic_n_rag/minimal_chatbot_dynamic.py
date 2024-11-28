import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # (if you have set it as an environment variable)
# client = OpenAI(api_key="sk-your-actual-key-here")  # Uncomment and replace with your actual key

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def chatbot_response(user_input, file_path):
    document_content = load_document(file_path)  # Reload the document content for each query
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Only answer questions with this document content: " + document_content},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def main():
    file_path = "yourdoc.txt"
    print("Hi, my name is Alfred and I'm your AI assistant! What can I help you with?")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Alfred: Thanks for chatting with me! Goodbye!")
            break
        response = chatbot_response(user_input, file_path)
        print("Alfred:", response)

if __name__ == "__main__":
    main()
