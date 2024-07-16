# Diet Scrapper

A program that uses selenium to scrap the meals from the diets provided by Maczfit (or any other company) and displays them as HTML web page.

## Getting started

Build a docker image from the [Dockerfile](./docker/Dockerfile):

```
$ cd ./docker
$ docker build --no-cache -t "diet_scrapper_docker" .
```

To build a docker image for the linux/arm64 platform (e.g. raspberry pi 4):

```
$ cd ./docker
$ docker buildx build --no-cache --platform linux/arm64 -t "diet_scrapper_docker" .
```

Run a docker container that contains the diet scrapper application available under `58253` port:

```
$ docker run -p 58253:58253 diet_scrapper_docker
```

### Deployment on Raspberry Pi 4B

Copy the docker image into the RPI:

```
$ docker save diet_scrapper_docker > diet_scrapper_docker.tar
$ scp diet_scrapper_docker.tar <username>@<ip_addr>:~/<path>
```

Log in to RPI via SSH and load the docker image:

```
$ docker load < diet_scrapper_docker.tar
```

... and run the docker container. Voila!