# Do arquivo Stack.py importe a Classe Stack
from Stack import Stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(30)

    print(f"{stack.pop()} foi removido da Pilha")
    print(f"{stack.pop()} foi removido da Pilha")
    print(f"{stack.pop()} foi removido da Pilha")
    print(f"{stack.pop()} foi removido da Pilha")
    print(f"O elemento do topo da Pilha é {stack.peek()}")