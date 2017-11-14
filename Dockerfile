FROM ubuntu:xenial

RUN \
  apt-get update && \
  apt-get install -y libjpeg-dev libpng12-dev build-essential libssl-dev libffi-dev \
  python python-dev python-pip python-virtualenv libxml2-dev libxslt1-dev vim cron \
  libtorrent-rasterbar8 python-libtorrent && \
  rm -rf /var/lib/apt/lists/*

ADD . /home/
WORKDIR /home/


