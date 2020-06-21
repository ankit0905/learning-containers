FROM python:3.6

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]