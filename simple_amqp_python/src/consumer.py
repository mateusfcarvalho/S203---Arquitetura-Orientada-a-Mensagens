#!/usr/bin/env python
import pika, sys, os
from datetime import datetime
from connection import AMQPConnection
import cryptocode

def callback(ch, method, properties, body):
    # The raw body is received in bytes, so is required to decode in UTF-8 format
    message = body.decode('utf-8')
    date_now = datetime.now().strftime('%d/%m/%Y %H:%M')

    CRYPTO_KEY = "teste"
    str_decoded = cryptocode.decrypt(message,CRYPTO_KEY)
    print(f"Mensagem recebida:\n-> {date_now}: {str(str_decoded)}")


def main():
    broker = AMQPConnection()

    print("[*] Aguardando por mensagens. Para sair digite: CTRL+C")
    broker.receive(callback)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Servidor de mensagens interrompido")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
