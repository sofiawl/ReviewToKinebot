from modelos.item_cardapio import ItemCardapio
from modelos.prato import Prato
from modelos.bebida import Bebida
from modelos.restaurante import Restaurante

def main():
  prato_normal = Prato('normal', 1.30, 'É um prato normal')
  suco_laranja = Bebida('suco de laranja', 5, 0.5)

  RU = Restaurante('Le Ru', [])

  RU.adicionar_cardapio(prato_normal)
  RU.adicionar_cardapio(suco_laranja)

  RU.exibir_cardapio()

  prato_normal.aplicar_desconto()
  suco_laranja.aplicar_desconto()

  RU.exibir_cardapio()
  

if __name__ == '__main__':
  main()