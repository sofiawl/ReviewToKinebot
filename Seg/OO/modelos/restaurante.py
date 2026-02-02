from .item_cardapio import ItemCardapio
from .bebida import Bebida
from .prato import Prato

class Restaurante(ItemCardapio):
  def __init__(self, nome, cardapio):
    self._nome = nome
    self._cardapio = []

  def adicionar_cardapio(self, item):
    if isinstance(item, ItemCardapio):
      self._cardapio.append(item)

  def exibir_cardapio(self):
    print(f'Cardapio do retaurante {self._nome}:')
    for i, item in enumerate(self._cardapio, start=1):
      if hasattr(item,'descricao'):
              mensagem_aux = f'| Descrição: {item.descricao}'
      else:
              mensagem_aux = f'| Litros: {item.litros}'

      mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco}' + mensagem_aux
      print(mensagem)
      
  def __str__(self):
    return print(f'nome\n')

'''
  def adicionar_bebida(self, bebida):
    self._cardapio.append(bebida)
  
  def adicionar_prato(self, prato):
    self._cardapio.append(prato)
'''