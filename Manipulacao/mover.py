import os

class Mover:
    def __init__(self):
        pass

    def mover_arquivo(self, origem, destino):
        if os.path.exists(origem):
            if not os.path.exists(destino):
                os.makedirs(destino)
                print(f'Pasta "{destino}" criada com sucesso!')

            caminho_destino = os.path.join(destino, os.path.basename(origem))
            os.rename(origem, caminho_destino)

            print(f'Arquivo "{os.path.basename(origem)}" movido para "{destino}"')
        else:
            print(f'Arquivo "{origem}" não encontrado!') 