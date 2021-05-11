class Cliente:
    '''
        self.nome = None
        self.celular = None
        self.endereco = None
        self.clientes = [None, None, None, None]

        def inserir(self):
        def mostrar(self):
    '''
    def __init__(self):
        self.nome = None
        self.celular = None
        self.endereco = None
        self.clientes = [None, None, None, None]

    def inserir(self):
        self.nome = input('Nome:')
        self.celular = input('Celular:')
        self.endereco = input('Endereco:')

    def mostrar(self):
        for c in self.clientes:
            print(f'Nome do cliente: {c.nome}')



