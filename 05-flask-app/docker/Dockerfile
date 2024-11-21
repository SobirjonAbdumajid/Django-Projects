FROM python:3.12.1

WORKDIR / app

COPY * /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]