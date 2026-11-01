# Self-contained image: any base works because the add-on does not use s6/bashio.
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/
COPY addon_run.py /app/addon_run.py

CMD ["python", "/app/addon_run.py"]
