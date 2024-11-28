import os
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # (if you have set it as an environment variable)
# client = OpenAI(api_key="sk-your-actual-key-here")  # Uncomment and replace with your actual key

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split('\n\n')  # Dela upp dokument i sektioner

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
            {"role": "system", "content": "Svara bara på frågor med det här dokumentinnehållet: " + relevant_section},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def main():
    document_sections = load_document("faq_hm.txt")
    print("Hej, jag heter Alfred och jag är din AI-assistent! Vad kan jag hjälpa dig med?")
    while True:
        user_input = input("\nDu: ")
        if user_input.lower() == "exit":
            print("Alfred: Tack för att du pratade med mig! Adjö!")
            break
        response = chatbot_response(user_input, document_sections)
        print("Alfred:", response)

if __name__ == "__main__":
    main()
