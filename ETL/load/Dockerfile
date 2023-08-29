FROM python:3.9-slim

WORKDIR /app

COPY /src /app/
COPY .env /app/
COPY tables.sql /app/
COPY requirements.txt /app/ 

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ] 