FROM python:3.8.0-slim

WORKDIR /stock-api
COPY . /stock-api

RUN pip3 install --no-cache-dir -r /stock-api/requirements.txt

CMD gunicorn src.main:app --bind 0.0.0.0:8000 \
        --workers ${GUNICORN_WORKERS_NUMBER:-1} \
        --threads ${GUNICORN_THREADS_NUMBER:-1} \
        --timeout ${GUNICORN_TIMEOUT_SECONDS:-300}
