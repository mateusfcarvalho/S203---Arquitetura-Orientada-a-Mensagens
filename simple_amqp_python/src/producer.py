#!/usr/bin/env python
import os, sys
from connection import AMQPConnection
import cryptocode

def main():
    broker = AMQPConnection()

    while True:
        message = input("Forneça a sua mensagem:\n->\t")
        CRYPTO_KEY = "teste"
        str_encoded = cryptocode.encrypt(message, CRYPTO_KEY)
        #print(f"Mensagem criptografada:\n-> {str_encoded}")
        broker.emit(str_encoded)
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Envio de mensagem finalizado!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
