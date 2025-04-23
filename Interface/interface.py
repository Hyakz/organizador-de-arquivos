from Manipulacao import Organizador
from Manipulacao import Mover
from Manipulacao import Renomear
from Utils import Arquivos
from Utils import Pastas

class Interface:
    def __init__(self):
        pass

    def exibir_menu(self):
        print("\n--- Menu de Opções ---\n")
        print("1. Organizar arquivos por extensão")
        print("2. Mover arquivo")
        print("3. Renomear arquivo")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")
        return opcao

    def organizar_arquivos(self):
        diretorio = input("Digite o diretório onde os arquivos estão localizados: ")
        organizador = Organizador()
        organizador.organizar_por_extensao(diretorio)

    def mover_arquivo(self):
        origem  = input("Digite o caminho do arquivo de origem: ")
        destino = input("Digite o caminho da pasta de destino: ")
        
        mover = Mover()
        mover.mover_arquivo(origem, destino)

    def renomear_arquivo(self):
        caminho   = input("Digite o caminho do arquivo a ser renomeado: ")
        novo_nome = input("Digite o novo nome do arquivo (sem a extensão): ")
        
        renomear = Renomear()
        renomear.renomear_arquivo(caminho, novo_nome)

    def listar_arquivos(self):
        diretorio = input("Digite o diretório para listar arquivos: ")
        arquivos  = Arquivos()
        lista     = arquivos.listar_arquivos(diretorio)
        
        print("Arquivos encontrados:")
        for arquivo in lista:
            print(arquivo)

    def criar_pasta(self):
        diretorio = input("Digite o diretório da pasta a ser criada: ")
        pastas = Pastas()
        pastas.criar_pasta(diretorio)