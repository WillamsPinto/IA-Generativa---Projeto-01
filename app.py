from api_manager import ApiManager
from chat_assistant import ChatAssistant

class App:
    def __init__(self):
        self.api_manager = ApiManager()
        self.chat_assistant = None

    def iniciar(self):
        # Carrega chave e inicializa modelo
        self.api_manager.carrega_chave()
        self.api_manager.inicializa_modelo()

        # Prepara o assistente
        chat_model = self.api_manager.obter_chat_model()
        self.chat_assistant = ChatAssistant(chat_model)
        self.chat_assistant.pre_treino()

        # Inicia a interação com o usuário
        self.iniciar_conversa()

    def iniciar_conversa(self):
        print("Assistente: Olá! Sou seu assistente de Classificação de Qualidade de Ovos. Qual imagem você gostaria de começar?")
        while True:
            entrada_usuario = input("Você: ")
            if entrada_usuario.lower() in ['sair', 'tchau', 'obrigado']:
                print("Assistente: Foi um prazer ajudar!")
                break
            self.chat_assistant.processar_entrada_usuario(entrada_usuario)

        # Exibir o histórico da conversa
        self.chat_assistant.exibir_historico()