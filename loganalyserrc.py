import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


datasethandle = pd.read_csv('rc3vshfut1.csv')

dataset = datasethandle.drop_duplicates()

#organização dos dados por interesse
zonadogol = dataset[dataset['ball_x'] > 36.00]
gols = dataset[dataset['playmode'] == 'goal_l']
escanteio = dataset[dataset['playmode'] == 'corner_kick_l']
prafora = dataset[dataset['playmode'] == 'goal_kick_l']

#definição dos atacantes
jogadoresrc = dataset.iloc[:,[0,1,10,11,18,19,28,34,49,50,59,65,80,81,90,96,111,112,121,127,142,143,152,158,173,174,183,189,204,205,214,220,235,236,245,251,266,267,276,282,297,298,307,313,328,329,338,344]]

player_x = dataset.iloc[:,[18,49,80,111,142,173,204,235,266,297,328]]
playerxcnames = player_x.columns
atacantes = []
index = 0
atacantesid = [0]
for column in playerxcnames:
    index +=1
    if jogadoresrc[jogadoresrc[str(column)] > 26].shape[0] > jogadoresrc[jogadoresrc[str(column)] < -26].shape[0]:
        atacantes.append(column)
        atacantesid.append(index)

        

#stamina dos atacantes
stamina_players = dataset.iloc[:,[1,28,59,90,121,152,183,214,245,276,307,338]]
stamina_atacantes = stamina_players.iloc[:,atacantesid]
goal_equipe = stamina_atacantes[stamina_atacantes['playmode'] == 'goal_l']
goal_oponente = stamina_atacantes[stamina_atacantes['playmode'] == 'goal_r']



#tempo ofensivo
atacantes.append('ball_x')
atacantestable = dataset.loc[:,atacantes]
bolazonf = atacantestable[atacantestable['ball_x'] > 26.00]
playersofensivos = bolazonf.drop('ball_x', axis=1)

def jogadaofensiva (linha):
    count = 0
    for celula in linha:
        if celula > 26:
            count += 1
    if count >= 3:
        return True
    else:
        return False

playersofensivos['ofensive'] = playersofensivos.apply(jogadaofensiva,axis=1)

tempoofensivo = playersofensivos[playersofensivos['ofensive'] == True]










