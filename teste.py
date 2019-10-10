from programa import *

filme = Filme('Esquadrão suicida', 2016, 120)
serie = Serie('The 100', 2018, 4)

filmes_e_series = [filme, serie] 

for programa in filmes_e_series:
    print('-=' *20)
    print(programa) 
