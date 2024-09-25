import os
import PIL.Image

class ChatAssistant:
    def __init__(self, chat_model):
        self.chat_model = chat_model

    def pre_treino(self):
        # Executa o pré-treino e armazena as mensagens enviadas no pré-treino
        print("Iniciando o Pré-treino...")

        self.chat_model.send_message("Você irá realizar classificações da Qualidade da Casca de Ovos de Galinha a Partir de Imagens de Ovoscopia. Então, você sempre deve receber Imagens com 15 ovos.")
        self.chat_model.send_message("Caso o usuário não lhe forneça uma imagem, você deve solicitar")
        self.chat_model.send_message("A saída deve ser uma classificação de 1 à 4, onde o 1 é o melhor e o 4 é o pior. Além disso, a saída deve ser sempre no formato de uma grade de 5x3, como por exemplo:\n1 1 1 1 1\n1 1 1 4 1\n1 2 2 2 1")
        self.chat_model.send_message("A ordem de classificação seria a seguinte:\n1: Ovos perfeitos\n2:Ovos com riscos de caneta\n3:Ovos Sujos\n4:Ovos quebrados ou trincados")

        self.chat_model.send_message("Uma classificação com todos os ovos perfeitos:\nclassificação: 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1")
        self.chat_model.send_message("Uma classificação com ovos riscados de caneta e ovos sujos:\nclassificação: 2 2 3 2 2\n1 2 3 3 2\n1 2 1 2 1")
        self.chat_model.send_message("Uma classificação com ovos trincados e ovos perfeitos:\nclassificação: 4 1 1 1 4\n1 1 1 4 1\n1 1 1 1 1")

        #disposicao = PIL.Image.open('Imagens/disposicaoOvos.png')
        #self.chat_model.send_message(["Utilize esta imagem como base para saber a disposição dos ovos na imagem da ovoscopia.", disposicao])
        self.chat_model.send_message("A leitura da imagem deve ser de cima para baixo, da esquerda para direita.\nSegue a ordem de leitura no formato 5x3:\n1º 4º 7º 10º 13º\n2º 5º 8º 11º 14º\n3º 6º 9º 12º 15º")

        imagem_exemplo1 = PIL.Image.open('Imagens/0 dias/IMG_0069-3.jpg')
        self.chat_model.send_message(["Essa imagem é um exemplo: O primeiro ovo está riscado com caneta, o segundo é um ovo perfeito, e o décimo primeiro está sujo.\nComo resultado, teriamos:\n2 1 1 1 1\n2 2 1 3 2\n2 2 1 2 2", imagem_exemplo1])

        imagem_exemplo2 = PIL.Image.open('Imagens/0 dias/IMG_0077-11.jpg')
        self.chat_model.send_message(["Outro exemplo: lendo da forma pré-estabelecida, ou seja, de cima para baixo, da esquerda para direita, temos:\nO primeiro ovo está levemente trincado\nDo segundo ao décimo são ovos sem defeitos\nO décimo primeiro está sujo.\nDo décimo segundo ao décimo quinto, são sem defeitos.\nComo resultado, teriamos:\n4 1 1 1 1\n1 1 1 3 1\n1 1 1 1 1", imagem_exemplo2])

        imagem_exemplo3 = PIL.Image.open('Imagens/0 dias/IMG_0074-8.jpg')
        self.chat_model.send_message(["Outro exemplo: O primeiro aparenta estar riscado\nO segundo não tem defeitos\nO terceiro tem um risco de caneta\nO quarto não tem defeito\nDo quinto ao nono, possuem riscos de caneta\nO décimo se encontra sujo\nO décimo primeiro está trincado\nO décimo segundo está riscado com caneta\nDo décimo terceiro ao décimo quinto, não tem defeitos.\nComo resultado, teriamos:\n2 1 2 3 1\n1 2 2 4 1\n2 2 2 2 1", imagem_exemplo3])

        imagem_exemplo4 = PIL.Image.open('Imagens/0 dias/IMG_0066-1.jpg')
        self.chat_model.send_message(["Classificação:\n1 1 1 1 1\n2 1 2 1 1\n2 2 2 1 2", imagem_exemplo4])

        imagem_exemplo5 = PIL.Image.open('Imagens/0 dias/IMG_0067-2.jpg')
        self.chat_model.send_message(["Classificação:\n1 2 1 1 1\n1 1 2 1 1\n2 2 2 2 2", imagem_exemplo4])

        imagem_exemplo6 = PIL.Image.open('Imagens/0 dias/IMG_0075-9.jpg')
        self.chat_model.send_message(["Classificação:\n2 1 1 1 1\n1 1 1 3 1\n1 2 1 2 2", imagem_exemplo4])

        imagem_exemplo7 = PIL.Image.open('Imagens/0 dias/IMG_0070-4.jpg')
        self.chat_model.send_message(["Classificação:\n1 3 2 1 1\n2 2 2 2 1\n2 2 2 1 1", imagem_exemplo4])

        imagem_exemplo8 = PIL.Image.open('Imagens/0 dias/IMG_0071-5.jpg')
        self.chat_model.send_message(["Classificação:\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1", imagem_exemplo4])

        imagem_exemplo9 = PIL.Image.open('Imagens/0 dias/IMG_0072-6.jpg')
        self.chat_model.send_message(["Classificação:\n1 1 1 1 1\n3 1 1 1 1\n3 1 1 1 1", imagem_exemplo4])

        imagem_exemplo10 = PIL.Image.open('Imagens/0 dias/IMG_0073-7.jpg')
        self.chat_model.send_message(["Classificação:\n1 1 1 1 1\n2 1 2 2 2\n1 2 2 2 2", imagem_exemplo4])

        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo1])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo2])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo3])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo4])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo5])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo6])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo7])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo8])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo9])
        self.chat_model.send_message(["Classifique esta imagem", imagem_exemplo10])

        print("Pré-treino realizado com sucesso!")

    def verificar_caminho_imagem(self, caminho):
        # Verifica se o caminho existe e é um arquivo
        if not os.path.exists(caminho):
            return False, "O caminho fornecido não existe."
        if not os.path.isfile(caminho):
            return False, "O caminho fornecido não é um arquivo."

        # Verifica se o arquivo é uma imagem
        try:
            PIL.Image.open(caminho).verify()  # Tenta abrir e verificar a imagem
        except (IOError, SyntaxError) as e:
            return False, "O arquivo fornecido não é uma imagem válida."

        return True, "Imagem válida."

    def processar_entrada_usuario(self, entrada_usuario):
        # Verifica se a entrada é um caminho para uma imagem
        valido, mensagem = self.verificar_caminho_imagem(entrada_usuario)
        if valido:
            # Se for uma imagem válida, realiza a classificação
            img = PIL.Image.open(entrada_usuario)
            resposta = self.chat_model.send_message(["Classifique esta imagem", img])
            print("Classificação:", resposta.text)
            return resposta.text
        else:
            # Se não for um caminho de imagem válido, trata como uma mensagem de texto
            response = self.chat_model.send_message(entrada_usuario)
            print("Assistente:", response.text)
            return response.text

    def exibir_historico(self):
        print("\nHistórico da Conversa:")
        for message in self.chat_model.history:
            print(f"{message.role}: {message.parts[0].text}")