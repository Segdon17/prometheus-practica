FROM python:3.10-slim

WORKDIR /app

# Copiar e instalar dependencias (se aprovecha la caché de Docker)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app/ .

EXPOSE 8000

# Comando para ejecutar la app con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]