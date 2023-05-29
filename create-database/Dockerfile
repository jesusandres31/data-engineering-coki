FROM python:3.12.0b1-alpine3.18

WORKDIR /app

COPY main.py /app/main.py
COPY tables.sql /app/tables.sql

RUN pip install psycopg2

CMD [ "python", "main.py" ]
