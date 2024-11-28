import os
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # (if you have set it as an environment variable)
# client = OpenAI(api_key="sk-your-actual-key-here")  # Uncomment and replace with your actual key

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split('\n\n')  # Splitting document into sections

def retrieve_relevant_section(query, document_sections):
    tfidf = TfidfVectorizer().fit_transform(document_sections)
    query_tfidf = TfidfVectorizer().fit(document_sections).transform([query])
    cosine_similarities = linear_kernel(query_tfidf, tfidf).flatten()
    relevant_section_index = cosine_similarities.argmax()
    return document_sections[relevant_section_index]

def chatbot_response(user_input, document_sections):
    relevant_section = retrieve_relevant_section(user_input, document_sections)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Only answer questions with this document content: " + relevant_section},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def main():
    document_sections = load_document("faq_hm.txt")
    print("Hi, my name is Alfred and I'm your AI assistant! What can I help you with?")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Alfred: Thanks for chatting with me! Goodbye!")
            break
        response = chatbot_response(user_input, document_sections)
        print("Alfred:", response)

if __name__ == "__main__":
    main()
