FROM python:3.11-alpine

ENV APP_DIR="/app" OUTPUT_DIR="/output" OUTPUT_FILE=".env" OUTPUT_FILE_KEY="WINDSCRIBE_EPHEMERAL_PORT"

WORKDIR ${APP_DIR}

COPY requirements.txt .

RUN python3 -m pip install -U pip
RUN python -m pip install -r requirements.txt

COPY src ./
VOLUME ["${OUTPUT_DIR}"]

CMD ["python3", "run.py"]
