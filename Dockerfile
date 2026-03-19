FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar codigo da aplicacao
COPY . .

# Expor porta
EXPOSE 8000

# Comando de inicializacao
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
