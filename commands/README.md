# Iniciar o projeto Django

```
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject projeto .
python manage.py startapp contact
```

# Configurar o git

```
git config --global user.name "seu_nome"
git config --global user.email "seu_email"
git config --global init.defaultBranch main
```

# Iniciar o git
```
git init
```

# Configurar o .gitignore
[djangowaves](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/)

# Adicionar e fazer o primeiro commit

```
git add .
git commit -m "First commit 🎉"
```

# configurar o repositório remoto
```
git remote add origin URL_DO_REPOSITÓRIO_GIT
```

# Migrando a base de dados do Django
```
python manage.py makemigrations
python manage.py migrate
```

# Criando e modificando a senha de um super usuário Django
```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```