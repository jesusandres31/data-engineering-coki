FROM python:3.9-slim
  
RUN apt-get update && \
    apt-get install -y mdbtools
 
WORKDIR /app

COPY export.py /app/

RUN pip install pyodbc

CMD ["python", "export.py", "--database", "/app/db/base.mdb"]
