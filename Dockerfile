FROM python:3.12-slim
LABEL authors="lharroyo"

# Establecer directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Exponer el puerto en el que correrá Flask
EXPOSE 8080

# Comando de inicio
CMD ["python", "main.py"]
