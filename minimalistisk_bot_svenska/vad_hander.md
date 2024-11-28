
# Ladda Dokument:
load_document läser innehållet från faq_hm.txt och sparar det som en sträng som chatboten kan använda för att svara på frågor.

# Generera Svar:
chatbot_response tar användarens fråga och FAQ-innehållet, skickar det till OpenAI API, och returnerar ett svar.

# Interaktiv Chatt:
I main körs chatboten i en oändlig loop där användaren kan skriva frågor. Om användaren skriver "exit" avslutas loopen.

# Att göra:
Spara koden som chat_bot.py.
Skapa en textfil som heter faq_hm.txt i samma mapp och fyll den med FAQ-innehåll.
Byt ut "your-openai-api-key" mot din riktiga API-nyckel från OpenAI.

# Exempel på interaktion:

Hej, jag heter Alfred och jag är HM's AI assistent! Vad kan jag hjälpa dig med?

Du: Vad är er returpolicy?
Alfred: Du kan returnera varor inom 30 dagar med kvitto.

Du: Hur spårar jag min beställning?
Alfred: Besök vår webbplats och logga in på ditt konto för att spåra din beställning.

Du: exit
Alfred: Tack för att du chattade med mig! Hejdå!