# Diet Scrapper

A program that uses selenium to scrap the meals from the diets provided by Maczfit (or any other company) and displays them as HTML web page.

## Getting started

Build a docker image from the [Dockerfile](./docker/Dockerfile):

```
$ cd ./docker
$ docker build -t "diet_scrapper_docker" .
```

Run a docker container that contains the diet scrapper application available under `58253` port:

```
$ docker run -p 58253:58253 diet_scrapper_docker
```