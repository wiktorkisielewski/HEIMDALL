# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code
ENV FLASK_APP=heimdall_app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
