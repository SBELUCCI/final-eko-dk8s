# Usamos la imagen oficial de PostgreSQL Alpine
FROM postgres:16-alpine

# No guardamos la contraseña en la imagen: se debe pasar al levantar el container
ENV POSTGRES_DB=appdb \
    POSTGRES_USER=appuser

# Copiamos el script de inicialización
COPY init.sql /docker-entrypoint-initdb.d/

# Exponemos el puerto por defecto de PostgreSQL
EXPOSE 5432

# Usamos el usuario por defecto de la imagen para seguridad
USER postgres

# Comando por defecto para arrancar PostgreSQL
CMD ["postgres"]

