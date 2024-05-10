FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
CMD ["python", "api_search.py"]

