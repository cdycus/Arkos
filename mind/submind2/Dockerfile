FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY mind .

CMD ["fastapi", "run", "app.py", "--port", "9002"]
