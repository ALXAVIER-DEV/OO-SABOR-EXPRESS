from modelos.avaliacao import Avaliacao
'''importa a classe Avaliacao do módulo modelos.avaliacao'''

class Restaurante:
    '''Classe para representar um restaurante'''    
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        '''Retorna uma representação em string do objeto Restaurante
        '''
        return  f' {self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Lista os restaurantes cadastrados
        '''
        print(f' {"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Media Avaliacoes".ljust(25)} | {"Status"}')
        for r in Restaurante.restaurantes:
            print(f' {r._nome.ljust(25)} | {r.categoria.ljust(25)} | {str(r.media_avaliacao).ljust(25)} | {r.status}')
                    
    @property
    def status(self):
        '''Retorna o status do restaurante
        Output: status atual do restaurante 
        '''
        return '⌧' if self._status else '☐'
        
    def alternar_status(self):
        '''Altera o status do restaurante
        '''
        self._status = not self._status
        
    def receber_avaliacao(self, usuario, nota, comentario):
        '''Recebe uma avaliação do restaurante
        '''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(usuario, nota, comentario)
            self._avaliacao.append(avaliacao)
               
    @property
    def media_avaliacao(self):
        '''Calcula a média das avaliações do restaurante
        Output: média das avaliações
        '''
        if not self._avaliacao:
            return '-'
        
       
        soma_das_notas = sum([a._nota for a in self._avaliacao])
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas,1)
        return media