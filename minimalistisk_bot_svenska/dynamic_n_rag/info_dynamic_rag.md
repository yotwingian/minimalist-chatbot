## Två modeller här:

#### - En dynamisk, där kontexten laddas varje gång en fråga ställs. Endast en rad tillagd:  
`document_content = load_document(file_path)`

#### - En andra med RAG-funktionalitet. Denna modell laddar också kontexten dynamiskt men delar upp dokumentet i sektioner, vilket förbättrar effektiviteten och relevansen för större datamängder. Använd detta tillvägagångssätt om du har en stor dataset!

#### - FAQ i denna katalog  har formaterats med 2 radbrytningar för att passa RAG.
