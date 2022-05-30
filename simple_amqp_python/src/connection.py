#!/usr/bin/env python
import pika



class AMQPConnection:
    URL = "amqps://trbqefii:UbAyYjeZd9php4j_UodHpXbxA9SfPKr0@woodpecker.rmq.cloudamqp.com/trbqefii"
    EXCHANGE = "prova_mateus"
    QUEUE = "prova_mateus"
    ROUTING_KEY = "task_queue"

    def __init__(self):
        self._start_connection()

    def emit(self, message):
        """[Receive a message and emit it to a broker using an open connection]

        Args:
            message (str): message to emit
        """
        if self.channel.is_closed:
            self._start_connection()
        
        self.channel.basic_publish(self.EXCHANGE,
                                    self.ROUTING_KEY,
                                    body=message)
        self._close()

    def receive(self, function_callback):
        """Responsible for setup the function to receive messages from the broker

        Args:
            function_callback (function): function that is responsible to handle the broker message
        """
        self.channel.basic_consume(queue=self.QUEUE,
                                    on_message_callback=function_callback,
                                    auto_ack=True)
        self.channel.start_consuming()

    def _start_connection(self):
        params = pika.URLParameters(self.URL)
        self.connection = pika.BlockingConnection(params)
        
        self.channel = self.connection.channel()
        self.channel.exchange_declare(self.EXCHANGE)
        self.channel.queue_declare(queue=self.QUEUE)
        self.channel.queue_bind(self.QUEUE, self.EXCHANGE, self.ROUTING_KEY)

    def _close(self):
        self.channel.close()
        self.connection.close()
