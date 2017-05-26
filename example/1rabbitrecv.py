#!/usr/bin/env python
import pika

auth = credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=auth))
channel = connection.channel()

channel.queue_declare(queue='hello2')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
