from programa import *
        
esquadrao = Filme('Esquadrão suicida', 2016, 120)
the_flash = Serie('The flash', 2018, 4)
chappie = Filme('Chappie', 2019, 130)

filmes_e_series = [esquadrao, the_flash, chappie] 

chappie.dar_liker()
chappie.dar_liker()
the_flash.dar_liker()
esquadrao.dar_liker()

playlist = Playlist('Filmes e séries', filmes_e_series) 
print('=-'*20)
print(f'Tamanho da playlist: {playlist.tamanho}')

for programa in playlist:
    print('-=' *20)
    print(programa) 
    
