FROM postgres:15.12
COPY script/db_init.sql /docker-entrypoint-initdb.d/
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=berlin_bike_theft_db
ENV PGDATA=/data