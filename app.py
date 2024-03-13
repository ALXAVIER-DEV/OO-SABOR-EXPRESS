from modelos.restaurantes import Restaurante

restaurante_baiano = Restaurante('o baiano', 'japonesa')
restaurante_baiano.receber_avaliacao('joao', 5, 'muito bom')
restaurante_baiano.receber_avaliacao('maria', 4, 'bom')
restaurante_baiano.receber_avaliacao('pedro', 3, 'regular')

restaurante_chines = Restaurante('o nordestino', 'nordestina')
restaurante_chines.receber_avaliacao('joao', 5, 'muito bom')
restaurante_chines.receber_avaliacao('maria', 8, 'bom')
restaurante_chines.receber_avaliacao('pedro', 5, 'regular') 

restaurante_chines = Restaurante('o chines', 'chinesa')

def main():
    Restaurante.listar_restaurantes()
    
if __name__ == '__main__':
    main()