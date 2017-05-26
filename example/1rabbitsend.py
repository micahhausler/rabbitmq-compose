#!/usr/bin/env python
import pika

auth = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=auth)
conn = pika.BlockingConnection(parameters)
channel = conn.channel()

channel.queue_declare(queue='hello2')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
conn.close()
