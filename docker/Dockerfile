FROM python:latest

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get -y update \
    && apt-get install -y google-chrome-stable \
    && apt-get install -yqq unzip \
    && pip install --upgrade pip \
    && pip install Django \
    && pip install selenium

RUN wget -O /tmp/chromedriver-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/`curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE`/linux64/chromedriver-linux64.zip \
    && unzip /tmp/chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/

RUN git clone https://github.com/piotr-tanski/diet-scrapper.git

COPY runserver.sh /usr/local/bin/runserver.sh
RUN chmod +x /usr/local/bin/runserver.sh

ENV DISPLAY=:99
CMD ["runserver.sh"]