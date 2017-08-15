FROM ubuntu:latest

# Update Ubuntu image
RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install GNURadio and UHD
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends gnuradio uhd-host && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*

# Install python prerequisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends python-setuptools python-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copied from python:onbuild
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./src/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src/ /usr/src/app

# Initialize database
RUN python2 manage.py makemigrations && python2 manage.py migrate