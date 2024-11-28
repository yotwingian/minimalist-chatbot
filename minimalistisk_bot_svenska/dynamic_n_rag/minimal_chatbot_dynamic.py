import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # (if you have set it as an environment variable)
# client = OpenAI(api_key="sk-your-actual-key-here")  # Uncomment and replace with your actual key

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def chatbot_response(user_input, file_path):
    document_content = load_document(file_path)  # Läs in dokumentinnehållet på nytt för varje fråga
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Svara bara på frågor med det här dokumentinnehållet: " + document_content},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def main():
    file_path = "yourdoc.txt"
    print("Hej, jag heter Alfred och jag är din AI-assistent! Vad kan jag hjälpa dig med?")
    while True:
        user_input = input("\nDu: ")
        if user_input.lower() == "exit":
            print("Alfred: Tack för att du pratade med mig! Adjö!")
            break
        response = chatbot_response(user_input, file_path)
        print("Alfred:", response)

if __name__ == "__main__":
    main()
