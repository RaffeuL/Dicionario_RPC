import xmlrpc.client
print("Dicionário Português")
while(True):
    palavra = input('Busque no Dicionário: ')
    with xmlrpc.client.ServerProxy("http://localhost:6565/") as proxy:
        significados = proxy.busca_palavra(palavra)
        print("##Todos os Siginificados: ")
        for significado in significados:
            print(significado)