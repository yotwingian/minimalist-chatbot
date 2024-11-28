from openai import OpenAI  
import os  

# Initiera OpenAI-klienten med hjälp av API-nyckeln från en miljövariabel.
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Alternativt kan du avkommentera nästa rad och ersätta "your-actual-key-here" med din faktiska OpenAI API-nyckel.
# client = OpenAI(api_key="sk-your-actual-key-here")

# Funktion för att ladda innehållet i ett dokument (FAQ-fil i det här fallet).
def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Funktion för att generera ett chatbot-svar baserat på användarens fråga och dokumentets innehåll.
def chatbot_response(user_input, document_content):
    # Skapa ett svar med hjälp av OpenAIs chat completion-API.
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Ange vilken modell som ska användas.
        messages=[
            # Systemmeddelande för att instruera chatboten att endast svara på frågor med hjälp av dokumentinnehållet.
            {"role": "system", "content": "Svara bara på frågor med det här dokumentinnehållet:" + document_content},
            # Användarens meddelande som innehåller användarens fråga.
            {"role": "user", "content": user_input}
        ]
    )
    # Returnera chatbotens svar.
    return response.choices[0].message.content

# Huvudfunktion för att köra chatboten.
def main():
    # Ladda innehållet i dokumentet (FAQ-filen).
    document_content = load_document("yourdoc.txt")
    # Skriv ut ett välkomstmeddelande.
    print("Hej, jag heter Alfred och jag är vår AI-assistent! Vad kan jag hjälpa dig med?")
    while True:
        # Få användarens inmatning.
        user_input = input("\nDu: ")
        # Om användaren skriver "exit", avsluta konversationen.
        if user_input.lower() == "exit":
            print("Alfred: Tack för att du pratade med mig! Adjö!")
            break
        # Generera ett svar från chatboten.
        response = chatbot_response(user_input, document_content)
        # Skriv ut chatbotens svar.
        print("Alfred:", response)

if __name__ == "__main__":
    main()

