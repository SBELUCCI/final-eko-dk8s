FROM postgres:16-alpine


ENV POSTGRES_DB=appdb \
POSTGRES_USER=appuser \
POSTGRES_PASSWORD=strongpassword


COPY init.sql /docker-entrypoint-initdb.d/


EXPOSE 5432