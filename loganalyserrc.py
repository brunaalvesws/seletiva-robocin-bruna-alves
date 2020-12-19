import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = input()

datasethandle = pd.read_csv(ds)
dataset = datasethandle.drop_duplicates()
timeesquerda = dataset.iloc[[0],[2]]
if (timeesquerda == 'RoboCIn').bool():
    #organização dos dados por interesse
    zonadogol = dataset[dataset['ball_x'] > 36.00].shape[0]
    gols = dataset[dataset['playmode'] == 'goal_l'].shape[0]
    escanteio = dataset[dataset['playmode'] == 'corner_kick_l'].shape[0]
    prafora = dataset[dataset['playmode'] == 'goal_kick_l'].shape[0]


    #grafico finalizações
    finalizacoes = pd.Series([zonadogol,escanteio,prafora,gols],index=['Linha do Ataque','Escanteio','Chute para fora','Gols'],name='Lances')
    finalizacoes.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(6, 6))
    plt.title('Finalizações e lances na linha do ataque')
    #plt.savefig('finalizações.png')
    plt.cla()


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
    goal_kick_equipe = stamina_atacantes[stamina_atacantes['playmode'] == 'goal_kick_l']
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
    tempoofensivo = playersofensivos[playersofensivos['ofensive'] == True].shape[0]
    temponaoofensivo = playersofensivos[playersofensivos['ofensive'] == False].shape[0]


    #graficos tempo ofensivo
    seriesofensive = pd.Series([tempoofensivo,temponaoofensivo],index=['Tempo ofensivo','Tempo não ofensivo'], name='Período do Jogo')
    seriesofensive.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(10, 6))
    plt.title('Tempo ofensivo e tempo não ofensivo em lances com a bola no campo adversário')
    #plt.savefig('tempoofensivozonadeataque.png')
    plt.cla()
    tempototal = dataset['show_time'].shape[0] - tempoofensivo
    seriestempototal = pd.Series([tempototal,tempoofensivo],index=['Tempo não ofensivo', 'Tempo ofensivo'],name='Período do Jogo')
    seriestempototal.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(6, 6))
    plt.title('Tempo ofensivo em relação ao tempo total de jogo')
    #plt.savefig('tempoofensivoxtotal.png')
    plt.cla()

    #posições de jogada ofensiva
    player_xy = dataset.iloc[:,[1,10,11,18,19,49,50,80,81,111,112,142,143,173,174,204,205,235,236,266,267,297,298,328,329]]
    nao_atacantes = 25 - (len(atacantes)-1)*2
    lista_atcxy = list(range(nao_atacantes,25))
    lista_atcxy.append(0)
    lista_atcxy.append(1)
    lista_atcxy.append(2)
    lista_atcxy.sort()
    atacantes_xy = player_xy.iloc[:,lista_atcxy]
    posicoes_gol = atacantes_xy[atacantes_xy['playmode']=='goal_l']
    pgcolunas = posicoes_gol.columns
    print(pgcolunas)
    for i in range(2,len(pgcolunas),2):
        posicoes_gol[pgcolunas[i]] = posicoes_gol[pgcolunas[i]]*-1

    def apagaduplicados(dataframe):
        aux = 0
        for i in dataframe.index:
            if i == aux+1:
                dataframe = dataframe.drop([i],axis=0)
            aux = i
        return dataframe

    posicoes_gollimpa = apagaduplicados(posicoes_gol)
    posicoes_gollimpa = posicoes_gollimpa.drop('playmode',axis=1)
    posicoesgoloponente = apagaduplicados(goal_oponente)
    posicoesgol_x = posicoes_gollimpa.iloc[:,list(range(0,len(posicoes_gollimpa.columns),2))]
    posicoesgol_y = posicoes_gollimpa.iloc[:,list(range(1,len(posicoes_gollimpa.columns),2))]


    #grafico posições de gol
    for i in range(len(posicoesgol_x.index)):
        plt.scatter(x=posicoesgol_x.iloc[i],y=posicoesgol_y.iloc[i],color=['red', 'green','green','green','green','green'])
        plt.axis([-56, 56, -35, 35])
        plt.title('Posição dos atacantes e da bola no lance do Gol')
        plt.xlabel('Coordenadas x do campo')
        plt.ylabel('Coordenadas y do campo')
        #plt.savefig('posiçãodegol'+ str(i)+'.png')
        plt.cla()


    #grafico stamina
    graficosstamina = stamina_atacantes.plot(figsize=(13, 8), subplots=True)
    for axes in graficosstamina:
        axes.plot([posicoes_gollimpa.index,posicoes_gollimpa.index], [0, 8000], color="black")
        axes.plot([posicoesgoloponente.index,posicoesgoloponente.index], [0, 8000], color="red")
    plt.xlabel('Tempo de Jogo')
    plt.ylabel('Valor do atributo Stamina')
    #plt.savefig('staminadosjogadores.png')

else:
    #organização dos dados por interesse
    zonadogol = dataset[dataset['ball_x'] > -36.00].shape[0]
    gols = dataset[dataset['playmode'] == 'goal_r'].shape[0]
    escanteio = dataset[dataset['playmode'] == 'corner_kick_r'].shape[0]
    prafora = dataset[dataset['playmode'] == 'goal_kick_r'].shape[0]


    #grafico finalizações
    finalizacoes = pd.Series([zonadogol,escanteio,prafora,gols],index=['Linha do Ataque','Escanteio','Chute para fora','Gols'],name='Lances')
    finalizacoes.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(6, 6))
    plt.title('Finalizações e lances na linha do ataque')
    plt.savefig('finalizações.png')
    plt.cla()



    #definição dos atacantes
    jogadoresrc = dataset.iloc[:,[0,1,10,11,359,360,369,375,390,391,400,406,421,422,431,437,452,453,462,468,483,484,493,499,514,515,524,530,545,546,555,561,576,577,586,592,607,608,617,623,638,639,648,654,669,670,679,685]]

    player_x = dataset.iloc[:,[359,390,421,452,483,514,545,576,607,638,669]]
    playerxcnames = player_x.columns
    atacantes = []
    index = 0
    atacantesid = [0]
    for column in playerxcnames:
        index +=1
        if jogadoresrc[jogadoresrc[str(column)] > -26].shape[0] > jogadoresrc[jogadoresrc[str(column)] < 26].shape[0]:
            atacantes.append(column)
            atacantesid.append(index)

            
    #stamina dos atacantes
    stamina_players = dataset.iloc[:,[1,369,400,431,462,493,524,555,586,617,648,679]]
    stamina_atacantes = stamina_players.iloc[:,atacantesid]
    goal_equipe = stamina_atacantes[stamina_atacantes['playmode'] == 'goal_r']
    goal_kick_equipe = stamina_atacantes[stamina_atacantes['playmode'] == 'goal_kick_r']
    goal_oponente = stamina_atacantes[stamina_atacantes['playmode'] == 'goal_l']


    #tempo ofensivo
    atacantes.append('ball_x')
    atacantestable = dataset.loc[:,atacantes]
    bolazonf = atacantestable[atacantestable['ball_x'] > -26.00]
    playersofensivos = bolazonf.drop('ball_x', axis=1)

    def jogadaofensiva (linha):
        count = 0
        for celula in linha:
            if celula > -26:
                count += 1
        if count >= 3:
            return True
        else:
            return False

    playersofensivos['ofensive'] = playersofensivos.apply(jogadaofensiva,axis=1)
    tempoofensivo = playersofensivos[playersofensivos['ofensive'] == True].shape[0]
    temponaoofensivo = playersofensivos[playersofensivos['ofensive'] == False].shape[0]


    #graficos tempo ofensivo
    seriesofensive = pd.Series([tempoofensivo,temponaoofensivo],index=['Tempo ofensivo','Tempo não ofensivo'], name='Período do Jogo')
    seriesofensive.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(10, 6))
    plt.title('Tempo ofensivo e tempo não ofensivo em lances com a bola no campo adversário')
    plt.savefig('tempoofensivozonadeataque.png')
    plt.cla()
    tempototal = dataset['show_time'].shape[0] - tempoofensivo
    seriestempototal = pd.Series([tempototal,tempoofensivo],index=['Tempo não ofensivo', 'Tempo ofensivo'],name='Período do Jogo')
    seriestempototal.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(6, 6))
    plt.title('Tempo ofensivo em relação ao tempo total de jogo')
    plt.savefig('tempoofensivoxtotal.png')
    plt.cla()

    #posições de jogada ofensiva
    player_xy = dataset.iloc[:,[1,10,11,359,360,390,391,421,422,452,453,483,484,514,515,545,546,576,577,607,608,638,639,669,670]]
    nao_atacantes = 25 - (len(atacantes)-1)*2
    lista_atcxy = list(range(nao_atacantes,25))
    lista_atcxy.append(0)
    lista_atcxy.append(1)
    lista_atcxy.append(2)
    lista_atcxy.sort()
    atacantes_xy = player_xy.iloc[:,lista_atcxy]
    posicoes_gol = atacantes_xy[atacantes_xy['playmode']=='goal_r']
    pgcolunas = posicoes_gol.columns
    for i in range(2,13,2):
        posicoes_gol[pgcolunas[i]] = posicoes_gol[pgcolunas[i]]*-1

    def apagaduplicados(dataframe):
        aux = 0
        for i in dataframe.index:
            if i == aux+1:
                dataframe = dataframe.drop([i],axis=0)
            aux = i
        return dataframe

    posicoes_gollimpa = apagaduplicados(posicoes_gol)
    posicoes_gollimpa = posicoes_gollimpa.drop('playmode',axis=1)
    posicoesgoloponente = apagaduplicados(goal_oponente)
    posicoesgol_x = posicoes_gollimpa.iloc[:,list(range(0,len(posicoes_gollimpa.columns),2))]
    posicoesgol_y = posicoes_gollimpa.iloc[:,list(range(1,len(posicoes_gollimpa.columns),2))]


    #grafico posições de gol
    for i in range(len(posicoesgol_x.index)):
        plt.scatter(x=posicoesgol_x.iloc[i],y=posicoesgol_y.iloc[i],color=['red', 'green','green','green','green','green'])
        plt.axis([-56, 56, -35, 35])
        plt.title('Posição dos atacantes e da bola no lance do Gol')
        plt.xlabel('Coordenadas x do campo')
        plt.ylabel('Coordenadas y do campo')
        plt.savefig('posiçãodegol'+ str(i)+'.png')
        plt.cla()


    #grafico stamina
    graficosstamina = stamina_atacantes.plot(figsize=(13, 8), subplots=True)
    for axes in graficosstamina:
        axes.plot([posicoes_gollimpa.index,posicoes_gollimpa.index], [0, 8000], color="black")
        axes.plot([posicoesgoloponente.index,posicoesgoloponente.index], [0, 8000], color="red")
    plt.xlabel('Tempo de Jogo')
    plt.ylabel('Valor do atributo Stamina')
    plt.savefig('staminadosjogadores.png')
