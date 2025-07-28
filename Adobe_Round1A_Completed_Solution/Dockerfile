
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app
COPY main.py .

RUN pip install --no-cache-dir pymupdf

CMD ["python", "main.py"]
