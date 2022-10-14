import requests
import json
from xmlrpc.server import SimpleXMLRPCServer


def busca_palavra(palavra):
    resposta = requests.get("https://significado.herokuapp.com/v2/" + palavra)
    significado = json.loads(resposta.content)
    return significado[0]['meanings']

server = SimpleXMLRPCServer(("localhost", 8000))
print("Rodando na porta 6565...")

server.register_function(busca_palavra, "busca_palavra")
server.serve_forever()

