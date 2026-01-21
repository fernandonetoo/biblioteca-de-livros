# 📚 Biblioteca de Livros – Django

O projeto desenvolvido foi desenvolvido utilizando o framework **Django**, seguindo o padrão **MVT (Model–View–Template)** com foco no gerenciamento de uma biblioteca de livros, explorando templates estáticos e dinâmicos, views e com persistência de dados em **PostgreSQL**.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- Django  
- PostgreSQL  
- Psycopg2  
- Python-dotenv  
- Git e GitHub  

---

## 🗂️ Estrutura do Projeto
```
atividade-MVT/
│
├── core/ # App principal
│ ├── models.py # Models da aplicação
│ ├── views.py # Views
│ └── ...
│
├── setup/ # Configurações do projeto Django
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── .env # Variáveis de ambiente (não versionado)
├── .gitignore
├── requirements.txt # Dependências do projeto
├── manage.py
└── README.md
```

---

## 🚀 Como usar:

### 1. Clonar o repositório

```bash
git clone 
```
https://github.com/fernandonetoo/biblioteca-de-livros.git


### 2. Criar e ativar a virtual environment
```
python manage.py venv venv
venv\Scripts\activate #Windowns
source venv/bin/activate #Linux
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure seu banco PostgreSQL no `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'biblioteca_de_livros',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Configuração das variáveis de Ambiente
```
DB_NAME=biblioteca_de_livros
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
```


### 6. Execute migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```

### 6. Acesse a aplicação

Visite [http://localhost:8000](http://localhost:8000) para ver a lista de livros.


📚 Objetivos de Aprendizado

- Aplicar o padrão MVT do Django

- Utilizar PostgreSQL com Django ORM

- Trabalhar com migrations

- Proteger dados sensíveis com .env

- Versionar dependências com requirements.txt

- Boas práticas com Git e GitHub
