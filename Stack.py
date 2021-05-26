# Do arquivo Node.py importe a Classe Nó
from Node import Node
# Classe Pilha
class Stack:
  # Inicializa a Pilha
  def __init__(self):
    self.root = None
  # Testa se a Pilha está Vazia
  def isEmpty(self):
    return True if self.root is None else False
  # Adiciona um nó na Fila
  def push(self, data):
    newNode = Node(data)
    newNode.next = self.root
    self.root = newNode
    print(f"{data} foi adionado na Pilha")
  # Remove um nó da Pilha e retorna o dado
  def pop(self):
    if (self.isEmpty()):
      return 'Pilha está Vazia.'
    temp = self.root
    self.root = self.root.next
    popped = temp.data
    return popped
  # Retorna o dado do topo da Pilha
  def peek(self):
    if self.isEmpty():
      return 'Pilha está Vazia.'
    return self.root.data
