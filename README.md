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
## Estrutura do projeto
   ```
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
```
## Configuração do Ambiente

**1. Adicione Aplicativos ao** ```INSTALLED_APPS```
Abra o arquivo ```settings.py``` dentro da pasta ```Django_Rest_Framework``` e adicione ```'rest_framework'``` e ```'app'``` à lista de ```INSTALLED_APPS```:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'app',
]
```
**2. Configure as URLs**
Abra o arquivo ```urls.py``` e configure as URLs da seguinte maneira:
```
from django.urls import path, include

urlpatterns = [
    path('api/', include('app.urls')),
]
```
## Modelos

No arquivo models.py, defina o modelo de Tarefa:
```
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

## Endpoints da API

Abaixo estão os endpoints disponíveis para interagir com a API. Cada endpoint permite realizar operações CRUD (Create, Read, Update, Delete) em tarefas.

### Listar Tarefas

- **Método**: `GET`
- **Endpoint**: `/api/tasks/`
- **Descrição**: Retorna uma lista de todas as tarefas.

#### Exemplo de Requisição

```http
GET /api/tasks/
```
#### Testes

Os testes podem ser escritos no arquivo tests.py da sua aplicação. Exemplo:
```
from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        Task.objects.create(title="Test Task", description="Test description")

    def test_task_creation(self):
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.description, "Test description")
```

### Referências

- Documentação do Django
- Documentação do Django Rest Framework

obs:Projeto feito para a Alura
