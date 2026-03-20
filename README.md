# 🧮 Calculadora API - Projeto SENAI

Uma API RESTful desenvolvida em Python utilizando o framework **FastAPI**. Este projeto está sendo construído de forma colaborativa, aplicando conceitos de arquitetura limpa, modularização de código e metodologias ágeis.

## 🚀 Funcionalidades Atuais

* **Operações Matemáticas Integradas:** Soma, Divisão, Raiz Quadrada e Multiplicação.
* **Arquitetura Modular:** Cada operação matemática foi desenvolvida de forma isolada por diferentes membros da equipe e integrada em um único ponto de entrada (`main.py`).
* **Documentação Interativa Automática:** Redirecionamento direto da rota raiz (`/`) para o painel visual de testes do Swagger UI (`/docs`), facilitando a usabilidade.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **FastAPI** (Framework Web para construção da API)
* **Uvicorn** (Servidor ASGI para rodar a aplicação)
* **Git & GitHub** (Versionamento e integração de código)

## ⚙️ Como rodar o projeto localmente

Siga os passos abaixo para testar a API na sua máquina:

1. Clone este repositório:
   ```bash
   git clone https://github.com/codebyaires/Desenvolvedores.git

Instale as bibliotecas necessárias:

Bash
pip install fastapi uvicorn
Inicie o servidor web:

Bash
python -m uvicorn main:app --reload
Teste a aplicação: Abra o seu navegador e acesse https://www.google.com/search?q=http://127.0.0.1:8000/. Você será redirecionado automaticamente para a interface de testes visuais da calculadora.

👨‍💻 Equipe de Desenvolvimento
Scrum Master / Integração Back-end: Victor Gabriel

Desenvolvedores (Lógica Matemática): Vitor Lucindo e Peterson Ruivo
