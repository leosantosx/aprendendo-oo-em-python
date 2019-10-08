from programa import *

filme = Filme('Esquadrão suicida', 2016, 120)
serie = Serie('The 100', 2018, 4)


serie.dar_liker() 
serie.nome = 'The flash' 

print(f'Nome: {filme.nome}\n'
      f'Ano: {filme.ano}\n'
      f'Duração: {filme.duracao}\n'
      f'Likes: {filme.likes}')
      
print('-='*20) 

print(f'Nome: {serie.nome}\n'
      f'Ano: {serie.ano}\n'
      f'Temporadas: {serie.temporadas}\n'
      f'Likes: {serie.likes}')
