# Organizador de Arquivos

Este projeto foi desenvolvido para organizar arquivos de diferentes tipos (extensões) em pastas específicas com base no tipo de arquivo. Ele permite que você organize arquivos de maneira simples e eficiente, separando-os por categorias como `css`, `html`, `js`, `json`, entre outros.

## Estrutura do Projeto

A estrutura de pastas e arquivos do projeto é a seguinte:

```
├── Arquivos/
├── Manipulacao/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── mover.py
│   ├── organizador.py
│   └── renomear.py
├── Utils/
│   ├── .gitignore
│   └── App.py
└── README.md
```

- **Arquivos/** contém os arquivos que usei para testar o funcionamento. 
- **Files/**: Contém os arquivos Python responsáveis por realizar a organização dos arquivos.
- **Utils/**: Contém utilitários adicionais para o funcionamento do projeto, como o arquivo `.gitignore` e o arquivo principal `App.py`.
- **README.md**: Este arquivo.

## Funcionalidades

O projeto oferece funcionalidades como:

- **Mover arquivos**: Organiza automaticamente os arquivos nas pastas correspondentes com base na sua extensão.
- **Renomear arquivos**: Renomeia arquivos conforme a convenção especificada.
- **Organizar arquivos**: A organização é feita de forma dinâmica e rápida, sem a necessidade de interação constante do usuário.

## Como Usar

1. Clone o repositório para sua máquina local:

   ```bash
   git clone <url-do-repositório>
   ```

2. Execute o programa com o comando:

   ```bash
   python App.py
   ```
   
3. O script organizará os arquivos nas pastas adequadas, com base nas suas extensões. Os arquivos podem estar em qualquer local da sua máquina.
