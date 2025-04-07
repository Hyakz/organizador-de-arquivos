from Utils.pastas            import Pastas
from Utils.arquivos          import Arquivos
from Manipulacao.organizador import Organizador
from Manipulacao.mover       import Mover
from Manipulacao.renomear    import Renomear

def exibir_menu():
    print("\n--- Menu de Opções ---")
    print("1. Organizar arquivos por extensão")
    print("2. Mover arquivo")
    print("3. Renomear arquivo")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")
    return opcao

def organizar_arquivos():
    diretorio   = input("Digite o diretório onde os arquivos estão localizados: ")
    organizador = Organizador()
    organizador.organizar_por_extensao(diretorio)

def mover_arquivo():
    origem  = input("Digite o caminho do arquivo de origem: ")
    destino = input("Digite o caminho da pasta de destino: ")
    
    mover = Mover()
    mover.mover_arquivo(origem, destino)

def renomear_arquivo():
    caminho   = input("Digite o caminho do arquivo a ser renomeado: ")
    novo_nome = input("Digite o novo nome do arquivo (sem a extensão): ")
    
    renomear = Renomear()
    renomear.renomear_arquivo(caminho, novo_nome)

def listar_arquivos():
    diretorio = input("Digite o diretório para listar arquivos: ")
    arquivos  = Arquivos()
    lista     = arquivos.listar_arquivos(diretorio)
    
    print("Arquivos encontrados:")
    for arquivo in lista:
        print(arquivo)

def criar_pasta():
    diretorio = input("Digite o diretório da pasta a ser criada: ")
    pastas = Pastas()
    pastas.criar_pasta(diretorio)

def main():
    opcoes = {
        '1': organizar_arquivos,
        '2': mover_arquivo,
        '3': renomear_arquivo,
        '4': lambda: print("Saindo do programa...") or exit()
    }

    while True:
        opcao = exibir_menu()

        if opcao in opcoes:
            opcoes[opcao]()  
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()