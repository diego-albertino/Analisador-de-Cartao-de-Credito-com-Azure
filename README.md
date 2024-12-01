# 📄 Analisador de Cartão de Crédito Anti-Fraude com Azure

## 📝 Descrição do Projeto

Este projeto visa implementar uma solução automatizada para análise de documentos utilizando Azure AI, com foco na identificação de padrões de fraude, validação de autenticidade e aumento da segurança em transações e processos empresariais. Utilizando técnicas avançadas de inteligência artificial e machine learning, a solução é capaz de detectar padrões suspeitos e anomalias em transações de cartões de crédito, proporcionando maior confiabilidade no processamento de documentos sensíveis e auxiliando na prevenção de fraudes.

### 🌐 Funcionalidades do Site

Foi desenvolvido um site local onde é possível fazer o upload da imagem do cartão de crédito. Após o upload, o serviço Azure AI Document Intelligence realiza a análise da imagem, verificando se é um cartão de crédito válido. O processo inclui a extração de informações relevantes da imagem, como:

- Número do cartão
- Data de validade
- Nome do titular

Utilizando técnicas avançadas de reconhecimento de padrões e machine learning, o sistema verifica a autenticidade do cartão e identifica possíveis fraudes, garantindo maior segurança nas transações.

### 🔍 Detalhes da Análise dos Cartões

A análise dos cartões envolve várias etapas, desde a extração de dados até a validação e verificação de autenticidade. O uso de Azure AI permite uma análise precisa e eficiente, contribuindo para a detecção de fraudes e a proteção de informações sensíveis.


## 🛠️ Tecnologias Utilizadas

- **Azure AI Document Intelligence**: Serviço da Azure que permite a extração de informações de documentos de forma automatizada, utilizando inteligência artificial para analisar e processar dados de maneira eficiente.
- **Azure Storage accounts**: Serviço de armazenamento da Azure que permite armazenar grandes volumes de dados de forma segura e escalável, essencial para armazenar os dados das transações de cartões de crédito que serão analisadas. 
- **Python**: Linguagem de programação utilizada para desenvolvimento dos scripts e integração com os serviços da Azure.

## 🎯 Objetivos

- Implementar uma solução automatizada para análise de transações de cartões de crédito.
- Detectar fraudes de maneira eficiente e precisa.
- Utilizar os serviços da Azure para garantir escalabilidade e robustez.

## 📄 Configuração do Ambiente

Para configurar o ambiente, siga os passos abaixo:

1. Crie um arquivo `.env` na raiz do projeto com base no arquivo `env.example`. Você pode copiar o conteúdo do `env.example` para o novo arquivo `.env` e ajustar as variáveis conforme necessário:

    ```bash
    cp env.example .env
    ```

2. Abra o arquivo `.env` e configure as variáveis de ambiente com os valores apropriados para sua configuração local. Certifique-se de definir as chaves de API e outras informações sensíveis corretamente.

Seguindo esses passos, você terá o ambiente configurado corretamente para executar o projeto.

## 🚀 Como Executar o Projeto

Para executar o projeto localmente, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do Python [aqui](https://www.python.org/downloads/).

2. Instale as dependências necessárias. Navegue até o diretório do projeto e execute o comando abaixo para instalar as bibliotecas listadas no arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute o aplicativo utilizando o Streamlit. No terminal, navegue até o diretório do projeto e execute o comando:

    ```bash
    streamlit run .\app.py
    ```

4. O Streamlit abrirá uma nova aba no seu navegador padrão, onde você poderá interagir com a aplicação e fazer o upload das imagens dos cartões de crédito para análise.

Seguindo esses passos, você conseguirá rodar o projeto localmente e testar todas as funcionalidades implementadas.
