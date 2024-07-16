FROM python:latest

RUN apt-get -y update \
    && apt-get install -y chromium \
    && apt-get install -y chromium-driver \
    && apt-get install -yqq unzip \
    && pip install --upgrade pip \
    && pip install Django \
    && pip install selenium

RUN git clone https://github.com/piotr-tanski/diet-scrapper.git

COPY runserver.sh /usr/local/bin/runserver.sh
RUN chmod +x /usr/local/bin/runserver.sh

ENV DISPLAY=:99
CMD ["runserver.sh"]