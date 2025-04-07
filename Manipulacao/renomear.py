import os

class Renomear:
    def __init__(self):
        pass

    def renomear_arquivo(self, caminho, novo_nome):
        if os.path.exists(caminho):
            _, extensao  = os.path.splitext(caminho)
            novo_caminho = os.path.join(os.path.dirname(caminho), novo_nome + extensao)

            os.rename(caminho, novo_caminho)
            print(f"Arquivo renomeado para {novo_caminho}")
        else:
            print(f"Erro: O arquivo {caminho} não foi encontrado.") 