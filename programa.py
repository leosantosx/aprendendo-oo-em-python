class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0
        
    @property
    def likes(self):
        return self._likes

    def dar_liker(self):
        self._likes += 1
        
    @property
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
        
class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
   