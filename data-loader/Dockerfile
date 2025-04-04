FROM python:3.10

WORKDIR /app

COPY ingest.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "ingest.py"]