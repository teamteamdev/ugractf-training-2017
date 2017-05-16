FROM jazzdd/alpine-flask:python3

ENV LIBRARY_PATH=/lib:/usr/lib
RUN apk update && apk add python3-dev build-base jpeg-dev zlib-dev && pip install qrcode Pillow
COPY app /app
