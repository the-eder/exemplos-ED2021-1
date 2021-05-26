# Do arquivo Stack.py importe a Classe Stack
from Stack import Stack

# Herdando classe Stack
class Pilha(Stack):

    def gera_dados(self, qtd):  # Gerando Dados Automaticamente
        [self.push(f'Fulano {n}') for n in range(qtd)]

    def imprimir_recursivo(self, no):  # Método recursivo
        # Base da chamada recursiva
        if (self.isEmpty()):
            return 'Pilha está Vazia.'

        # O parametro end='-> ' é defido o padrão é end='\n'
        print(no.data, end='-> ')

        # Base da chamada recursiva
        if no.next == None:
            print('NULL')
            return

        # Faz a chamada recursiva
        self.imprimir_recursivo(no.next)

if __name__ == "__main__":
    pilha = Pilha()
    pilha.gera_dados(10)
    pilha.imprimir_recursivo(pilha.root)