from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # (if you have set it as an environment variable)
# client = OpenAI(api_key="sk-your-actual-key-here")  # Uncomment and replace with your actual key

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def chatbot_response(user_input, document_content):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Only answer questions with this document content: " + document_content},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def main():
    document_content = load_document("faq_hm.txt")
    print("Hi, my name is Alfred and I'm our AI assistant! What can I help you with?")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Alfred: Thanks for chatting with me! Goodbye!")
            break
        response = chatbot_response(user_input, document_content)
        print("Alfred:", response)

if __name__ == "__main__":
    main()
