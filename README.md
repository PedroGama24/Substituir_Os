# Substituir Serviços

Este é um aplicativo web simples desenvolvido em Flask que permite substituir textos em uma lista de serviços e baixar o resultado em um arquivo CSV.

## Estrutura do Projeto

```filetree
simple-web-app
├── src
│   ├── app.py              # Arquivo principal da aplicação
│   ├── templates
│   │   └── index.html      # Template HTML para entrada do usuário
│   └── static
│       └── styles.css      # Estilos CSS para a aplicação
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto



Crie um ambiente virtual e ative-o:
    #python -m venv venv
    #source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:
    #pip install -r requirements.txt

Execução:
    Execute o aplicativo:
        python src/app.py
    Abra o navegador e acesse:
        http://localhost:5000

Uso:
    Insira os serviços na área de texto fornecida.
    Clique no botão "Processar".
    O arquivo lista_transformada.csv será gerado e baixado automaticamente.