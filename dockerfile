FROM python:3.7-alpine
# Create app directory

RUN apk add build-base python3-dev py-pip jpeg-dev zlib-dev freetype-dev
ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR /home/python/app

RUN pip3 install --no-cache-dir Flask python-barcode "python-barcode[images]"

COPY server.py ./

EXPOSE 5000

CMD [ "python", "server.py" ]
