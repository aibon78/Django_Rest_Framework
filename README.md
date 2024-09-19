# Documentação do Projeto: Django Rest Framework Study Project

## Índice

1. [Visão Geral](#visão-geral)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação](#instalação)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Configuração do Ambiente](#configuração-do-ambiente)
6. [Modelos](#modelos)
7. [Endpoints da API](#endpoints-da-api)
8. [Testes](#testes)
9. [Referências](#referências)

## Visão Geral

Este projeto tem como objetivo estudar e implementar uma API RESTful utilizando o Django Rest Framework. O projeto simula um sistema de gerenciamento de tarefas, permitindo criar, listar, atualizar e excluir tarefas.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado:

- Python (3.6 ou superior)
- pip (gerenciador de pacotes do Python)
- Django
- Django Rest Framework

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/Django_Rest_Framework.git
   cd Django_Rest_Framework
   ```
2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install django djangorestframework
   ```
4. Crie e aplique as migrações:
   ```
   python manage.py migrate
   ```
5.Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```
# Estrutura do projeto
   
   Django_Rest_Framework/
   │
   ├── manage.py
   ├── venv/
   │
   ├── app/
   │   ├── migrations/
   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── serializers.py
   │   ├── tests.py
   │   └── views.py
   │
   └── Django_Rest_Framework/
       ├── __init__.py
       ├── settings.py
       ├── urls.py
       └── wsgi.py

