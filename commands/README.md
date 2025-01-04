# Iniciar o projeto Django

```bash
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject projeto .
python manage.py startapp contact
```

# Configurar o git

```bash
git config --global user.name "seu_nome"
git config --global user.email "seu_email"
git config --global init.defaultBranch main
```

# Iniciar o git
```bash
git init
```

# Configurar o .gitignore
[djangowaves](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/)

# Adicionar e fazer o primeiro commit

```bash
git add .
git commit -m "First commit 🎉"
```

# configurar o repositório remoto
```bash
git remote add origin URL_DO_REPOSITÓRIO_GIT
```

# Migrando a base de dados do Django
```bash
python manage.py makemigrations
python manage.py migrate
```

# Criando e modificando a senha de um super usuário Django
```bash
python manage.py createsuperuser
python manage.py changepassword USERNAME
```

# Trabalhando com o model do Django
```python
# Importe o módulo
from django.modles import Contact

# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()

# Cria um contato (Não Lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)

# Seleciona um contato com o id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)

# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()

# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()

# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')

# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
```