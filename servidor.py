from dicio import Dicio
import requests
import json
from xmlrpc.server import SimpleXMLRPCServer


# def is_even(n):
#     dicio = Dicio()
#     print("Requisição recebida com o seguinte argumentoooo: " + n)
#     word = dicio.search(n)
#     return [word.meaning, word.etymology]
# server = SimpleXMLRPCServer(("localhost", 8000))

# print("Listening on port 8000...")

# server.register_function(is_even, "is_even")
# server.serve_forever()

def busca_palavra(palavra):
    resposta = requests.get("https://significado.herokuapp.com/v2/" + palavra)
    significado = json.loads(resposta.content)
    return significado[0]['meanings']

#     dicio = Dicio()
#     print("Requisição recebida com o seguinte argumentoooo: " + n)
#     word = dicio.search(n)
#     return [word.meaning, word.etymology]
server = SimpleXMLRPCServer(("localhost", 8000))

print("Listening on port 8000...")

server.register_function(busca_palavra, "busca_palavra")
server.serve_forever()

