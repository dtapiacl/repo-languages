FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install requests

CMD ["python", "fetch_languages.py"]