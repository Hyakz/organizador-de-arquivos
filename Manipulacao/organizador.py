import os
from Utils import Pastas
from Utils import Arquivos

class Organizador:
    def __init__(self):
        self.pastas = Pastas()
        self.arquivos = Arquivos()
    
    def organizar_por_extensao(self, diretorio):
        arquivos = self.arquivos.listar_arquivos(diretorio)

        for arquivo in arquivos:
            _, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower().replace('.', '') 

            if extensao:  
                pasta_destino = os.path.join(diretorio, extensao)
                self.pastas.criar_pasta(pasta_destino)

                caminho_origem  = os.path.join(diretorio, arquivo)
                caminho_destino = os.path.join(pasta_destino, arquivo) 

                if not os.path.exists(caminho_destino):
                    os.rename(caminho_origem, caminho_destino)
                    print(f'Arquivo "{arquivo}" movido para "{pasta_destino}"')
                else:
                    print(f'O arquivo "{arquivo}" já está na pasta "{pasta_destino}"')
            else:
                pasta_destino = os.path.join(diretorio, "sem_extensao")
                self.pastas.criar_pasta(pasta_destino)

                caminho_origem  = os.path.join(diretorio, arquivo)
                caminho_destino = os.path.join(pasta_destino, arquivo)

                if not os.path.exists(caminho_destino):
                    os.rename(caminho_origem, caminho_destino)
                    print(f'Arquivo "{arquivo}" movido para "sem_extensao"')
                else:
                    print(f'O arquivo "{arquivo}" já está na pasta "sem_extensao"')
 