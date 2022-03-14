FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -U pip \ 
        && pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]