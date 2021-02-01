FROM python:3.7

LABEL maintainer="Carlos Garzon <cgarzon@grupodot.com>"

ENV PORT=8000
ENV USER=worker

RUN pip install --upgrade pip

RUN groupadd -r $USER && useradd -r -s /bin/false -g $USER $USER
WORKDIR /home

COPY --chown=$USER:$USER requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=$USER:$USER /app ./app/

EXPOSE $PORT

CMD python app/main.py