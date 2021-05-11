from TAD_Cliente import Cliente

if __name__ == '__main__':
    lista_de_clientes = Cliente()
    for indice in range(4):
        novo_cliente = Cliente()
        novo_cliente.inserir()
        lista_de_clientes.clientes[indice] = novo_cliente

    lista_de_clientes.mostrar()