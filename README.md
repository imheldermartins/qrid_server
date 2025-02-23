# Django + Docker + Postgres 
### (Working on Windows 11)

## Setup

```sh
# Create virtual enviroment to build own project
python -m venv /venv

# Activate venv on terminal
source venv/Scripts/activate

# Install all required packages
pip install django gunicorn psycopg2-binary

# After installed packages, we need put them into requirements.txt file
pip freeze > requirements.txt
```

Não instale o "pacote "~~libpq-dev~~, ele é do ambiente linux.

```sh
sudo apt-get install libpq-dev
```

## Django: Quick Start

```sh
# Start a project
django-admin startproject <project_name | or core_name> ./destination_folder

# Testing django server
python manager.py runserver
```

# Docker Setup

```Dockerfile
FROM python:3.14.0a5-slim-bullseye

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV PYTHONPATH=/app

# Definir o diretório de trabalho
WORKDIR /app

# **Instalar dependências do sistema antes de instalar os pacotes Python**
RUN apt-get update && apt-get install -y \
    libpq-dev gcc build-essential python3-dev

# Copiar e instalar as dependências do Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o restante do código do projeto para o contêiner
COPY . /app/

# Comando para iniciar o servidor Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8080"]

# Expor a porta que o servidor usará
EXPOSE ${PORT}
```

```sh
# Build image for contâiner
docker build --no-cache -t senior-server:latest .

# Create contâiner and run with enviroments variables - Production
docker run -p 8000:8080 \
--env PIPELINE=production \
--env SECRET_KEY=your_value \
--env DB_NAME=. \
--env DB_USER_NM=. \
--env DB_USER_PW=. \
--env DB_HOST=0.0.0.0 \
--env DB_PORT=5432 \
senior-server
```

