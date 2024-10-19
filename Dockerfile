# Usa una imagen de Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación a /app
COPY . .

# Exponer el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 80

# Ejecutar el servidor de desarrollo (o usar gunicorn para producción)
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
