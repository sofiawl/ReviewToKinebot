from .item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
  def __init__(self, nome, preco, litros):
    super().__init__(nome, preco)
    self.litros = litros
  
  def aplicar_desconto(self):
    self._preco -= (self._preco * 0.05)

  def __str__(self):
    return "{}, litros: {}".format(super().__str__(), self.litros)

