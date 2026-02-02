from .item_cardapio import ItemCardapio

class Prato(ItemCardapio):
  def __init__(self, nome, preco, descricao):
    super().__init__(nome, preco)
    self.descricao = descricao

  def aplicar_desconto(self):
    self._preco -= (self._preco * 0.08)
  
  def __str__(self):
    return "{}, descrição: {}".format(super().__str__(), self.descricao)

