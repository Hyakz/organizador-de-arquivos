import os

class Pastas:
    def __init__(self):
        pass

    def criar_pasta(self, diretorio):
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f'Pasta "{diretorio}" criada com sucesso!')
        else:
            print(f'A pasta "{diretorio}" já existe!')

    def listar_pastas(self, diretorio):
        return [f for f in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, f))]

    def remover_pasta(self, diretorio):
        if os.path.exists(diretorio) and not os.listdir(diretorio):
            os.rmdir(diretorio)
            print(f'Pasta "{diretorio}" removida com sucesso!')
        else:
            print(f'A pasta "{diretorio}" não existe ou não está vazia!')

    def renomear_pasta(self, caminho_antigo, caminho_novo):
        if os.path.exists(caminho_antigo):
            os.rename(caminho_antigo, caminho_novo)
            print(f'Pasta renomeada de "{caminho_antigo}" para "{caminho_novo}".')
        else:
            print(f'A pasta "{caminho_antigo}" não existe!')

    def verificar_pasta(self, diretorio):
        return os.path.exists(diretorio)

    def verificar_pasta_vazia(self, diretorio):
        if os.path.exists(diretorio):
            return len(os.listdir(diretorio)) == 0
        return False