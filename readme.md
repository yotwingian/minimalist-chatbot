# Minimalistic OpenAI Chatbot

- This repo helps you set up a minimalistic chatbot using OpenAI's API, which answers questions based on a document.
- There are 5 diffrent models one can draw inspiration and knowlege off, two of them in jupyter .
- A Swedish language support directory ( same stuff in swedish)


## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/minimalist-chatbot.git
    cd minimalist-chatbot
    ```

2. **Install Required Packages**
  The easyst example only uses openai lib.
  
  
   Libs: openai
         sklearn
         ipywidgets    

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare Your Document**
    Ensure you have a text file named `yourdoc.txt` with your  content in the same directory as `minimal_chatbot.py`.

2. **Set Up Your OpenAI API Key**
    Set your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY=your-openai-api-key
    ```

3. **Run the Chatbot**
    ```bash
    python minimal_chatbot.py
    ```

4. **Interact with the Chatbot**
    Open your console and start interacting with the chatbot by typing your questions.

## Example

```bash
Hi, my name is Alfred and I'm our AI assistant! What can I help you with?

Du: What are your opening hours?
Alfred: The store is open from 9 AM to 9 PM.
