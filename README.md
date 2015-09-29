# RabbitMQ in docker-compose

## Setup
This setup assumes you already have docker-compose and docker (using docker toolbox) installed.

```
git clone git@github.com:micahhausler/rabbitmq-compose.git
cd rabbitmq-compose
docker-compose up
```

## Play
Open [http://192.168.59.103:15672/](http://192.168.59.103:15672/) (or what ever IP you get when you run `docker-machine ip`)

```
open http://$(docker-machine ip default):15672/
```
and use the login

```
username: rabbitmq
password: rabbitmq
```

## License
MIT License
