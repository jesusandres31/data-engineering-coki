FROM debian:latest

# Instalar las dependencias necesarias
RUN apt-get update && \
    apt-get install -y mdbtools

# Copiar los archivos necesarios al contenedor
COPY export.py /app/

# Establecer el directorio de trabajo
WORKDIR /app

# Ejecutar el script al iniciar el contenedor
CMD ["python", "export.py"]
