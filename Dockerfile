FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY dev-requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
	pip install --no-cache-dir -r dev-requirements.txt

COPY main.py ./main.py
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
