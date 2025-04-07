FROM python:3.10

WORKDIR /app

COPY /data/lor_planungsraeume.xlsx /data/bezirke.csv /data/bezirksregionen.csv /data/planungsraeume.csv /data/prognoseraeume.csv ./

COPY ingest.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "ingest.py"]