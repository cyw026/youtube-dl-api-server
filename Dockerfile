FROM python:2.7

ADD . /code
WORKDIR /code
COPY requirements.txt /code
EXPOSE 9191
RUN pip install -r requirements.txt
RUN python -m youtube_dl_serve