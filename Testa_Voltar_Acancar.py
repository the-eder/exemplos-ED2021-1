# Do arquivo Stack.py importe a Classe Stack
from Stack import Stack
# Importe
import webbrowser

if __name__ == "__main__":
  url_voltar = Stack() # Pilha para Voltar
  url_avancar = Stack() # Pilha para Avaçar

  # Abrindo as péginas
  url_voltar.push('https://www.google.com/')
  url_voltar.push('https://www.globo.com/')
  url_voltar.push('http://www.ic.uff.br/index.php/pt/pos-graduacao/linhas-de-pesquisa#CV')

  # Clicando em voltar duas vezes
  url_avancar.push(url_voltar.pop())
  url_avancar.push(url_voltar.pop())

  # Clicando em Avançar uma vez
  url_voltar.push(url_avancar.pop())
  url_voltar.push(url_avancar.pop())

  # Mostrando resultado no Navegador
  webbrowser.open(url_voltar.peek()) # Só vai rodar na linha de comando