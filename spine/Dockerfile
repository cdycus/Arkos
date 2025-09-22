FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ../brain .

CMD ["fastapi", "run", "api.py", "--port", "8000"]
