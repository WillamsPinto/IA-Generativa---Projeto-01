from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import os

class ApiManager:
    def __init__(self):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 1024,
            "response_mime_type": "text/plain",
        }
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        self.model = None
        self.chat_model = None

    def carrega_chave(self):
        _ = load_dotenv(find_dotenv())
        chave = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=chave)
        print("Chave API carregada com sucesso!")
        return chave

    def inicializa_modelo(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            safety_settings=self.safety_settings,
            generation_config=self.generation_config,
        )
        self.chat_model = self.model.start_chat(history=[])
        print("Modelo inicializado com sucesso!")

    def obter_chat_model(self):
        return self.chat_model