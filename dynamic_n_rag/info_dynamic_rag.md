## Two models here:

### one dynamic, meaning the context is loaded each time a query is asked. just  one row added : 
`document_content = load_document(file_path)`

### second with RAG functionality ,This model also loads the context dynamically but divides the document into sections, enhancing efficiency and relevance for larger datasets. Use this approch if you have a big dataset!

### The ffq in this dir has been formatted with 2 line breaks to fitt RAG
