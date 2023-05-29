FROM python:3.9-slim

WORKDIR /app

COPY main.py /app/main.py 
COPY .env /app/.env 
COPY tables.sql /app/tables.sql
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ] 