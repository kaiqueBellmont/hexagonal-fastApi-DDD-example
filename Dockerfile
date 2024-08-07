# Usando uma imagem base Python
FROM python:3.9

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos de requirements
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante do código da aplicação
COPY . .

# Executando a aplicação
CMD ["uvicorn", "app.adapters.entrypoints.application:app", "--reload", "--host",  "0.0.0.0", "--port", "8000"]
