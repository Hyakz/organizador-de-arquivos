import os

class Arquivos:
    def __init__(self):
        pass

    def listar_arquivos(self, diretorio):
        return [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]

    def filtrar_por_extensao(self, diretorio, extensao):
        arquivos = self.listar_arquivos(diretorio)
        return [f for f in arquivos if f.lower().endswith(f'.{extensao.lower()}')]

    def verificar_arquivo(self, caminho_arquivo):
        return os.path.exists(caminho_arquivo)