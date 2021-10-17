FROM python:3.7-slim

LABEL maintainer="Carlos Garzon <gagocaan@gmail.com>"

ENV PORT=8000
ENV USER=worker

RUN pip install --upgrade pip

RUN groupadd -r $USER && useradd -r -s /bin/false -g $USER $USER
WORKDIR /home

COPY --chown=$USER:$USER pyproject.toml .
RUN pip install poetry
RUN poetry install

COPY --chown=$USER:$USER /app ./app/

EXPOSE $PORT

CMD poetry run python app/main.py