from Interface.interface import Interface

class Main:
    def __init__(self):
        self.interface = Interface()

    def start(self):
        opcoes = {
            '1': Interface.organizar_arquivos,
            '2': self.interface.mover_arquivo,
            '3': self.interface.renomear_arquivo,
            '4': lambda: print("Saindo do programa...") or exit()
        }

        try:
            while True:
                opcao = self.interface.exibir_menu()

                if opcao in opcoes:
                    opcoes[opcao]()  
                else:
                    print("Opção inválida! Tente novamente.")
        except KeyboardInterrupt:
            print("\nAplicação Finalizada...")
            exit()

if __name__ == "__main__":
    main = Main()
    main.start()