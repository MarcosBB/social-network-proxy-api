# social-network-proxy-api



## Configurações 
Crie na raiz do projeto o arquivo `.env` e introduza nele as informações necessárias a conexão com o servidor do rabbitMQ e com o banco de dados, abaixo a lista das informações:

```env
# RabbitMQ
RABBITMQ_HOST=
RABBITMQ_PORT=
RABBITMQ_USERNAME=
RABBITMQ_PASSWORD=

# Database
DATABASE_NAME=
```

## Execução
1. Iniciar uma instância do servidor RabbitMQ
2. Executar `pip install -r requirements.txt` para instalar os requisitos na sua máquina
3. Rode o arquivo `api.py` para a api começar a rodar.
4. Em outro terminal rode o arquivo `client.py` para iniciar o client.

## Autores
- [Marcos Barros](https://github.com/MarcosBB)
- [Gdiael Barros](https://github.com/gdiael)