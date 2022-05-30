# Introdução
Projeto da disciplina de Arquitetura e Desenhos de Software do curso de Engenharia de Software para demostrar o Padrão de Arquitetura Orientada a Mensagens através do protocolo AMQP, fazendo uso da implementação RabbitMQ.

## Tecnologia
Este projeto utiliza a linguagem de programação Python versão 3.x e o driver de comunicação AMQP para Python -> Pika 1.2.0.
## Referência
Projeto baseado no tutorial: https://www.cloudamqp.com/blog/how-to-run-rabbitmq-with-python.html e modificado para atender as necessidades da disciplina.

## Descrição
O projeto possui a implementação de dois programas:
- consumer.py: responsável por receber mensagens, de forma assíncrona, do broker AMQP e exibí-la no console;
- producer.py: responsável por captar mensagens do usuário e enviá-las para o broker AMQP, o qual se encarregará de entregá-la aos consumidores.


# Ambiente para Execução
## Message Broker
Além do projeto local é necessário tem um Message Broker AMQP, pra isso você pode utilizar o RabbitMQ, disponível para download em: https://www.rabbitmq.com/. 
Caso não queira instalar um broker na sua máquina local, você pode configurar e consumir uma versão na nuvem, através de uma conta grátis no CloudAMQP: https://www.cloudamqp.com/
## Configuração do Projeto
Primeiramente você precisará ter o Python versão 3.x instalado em sua máquina. Com isso poderá criar uma VirtualEnv para a instalação do driver para comunicar com o protocolo AMQP. Para isso utilize o Prompt do Windows ou um Terminal de linha de comando, para acessar o diretório no qual você clonou (ou fez download) o projeto.

Crie a VirtualEnv:
- ```python -m venv <<nome da virtual env>>```

Agora instale as dependências do projeto
- ```pip install -r requirements.txt```

# Executar
## Consumidor
Para executar o programa capaz de consumir dados de uma fila AMQP, execute o módulo consumer.py:
- ```python consumer.py```

## Produtor
Para executar o programa capaz de enviar mensagens para uma fila AMQP, execute o módulo producer.py:
- ```python producer.py```
