from dicio import Dicio
import xmlrpc.client
palavra = input('digita uma palavra ai: ')
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    significados = proxy.busca_palavra(palavra)
    print("Siginificados: ")
    for significado in significados:
        print(significado)