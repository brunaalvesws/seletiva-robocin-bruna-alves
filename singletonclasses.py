import pandas as pd
import matplotlib.pyplot as plt


class gameObject:

    _instance = None

    def __init__(self,dataframe):
        self.dataset = dataframe

    @classmethod
    def instance(cls,dataframe):
        if cls._instance is None:
            cls._instance = cls(dataframe)
        return cls._instance

    def duplicidade (self):
        ds = self.dataset.drop_duplicates()
        return ds

    def zonadogol_l(self):
        nzonadogol = self.dataset[self.dataset['ball_x'] > 36.00].shape[0]
        return nzonadogol

    def gols_l(self):
        ngols = self.dataset[self.dataset['playmode'] == 'goal_l'].shape[0]
        return ngols

    def golsoponente_l(self):
        ngols = self.dataset[self.dataset['playmode'] == 'goal_r'].shape[0]
        return ngols

    def escanteio_l(self):
        nescanteio = self.dataset[self.dataset['playmode'] == 'corner_kick_l'].shape[0]
        return nescanteio

    def prafora_l(self):
        nprafora = self.dataset[self.dataset['playmode'] == 'goal_kick_l'].shape[0]
        return nprafora

    def jogadores_l(self):
        njogadores = self.dataset.iloc[:,[0,1,10,11,18,19,28,34,49,50,59,65,80,81,90,96,111,112,121,127,142,143,152,158,173,174,183,189,204,205,214,220,235,236,245,251,266,267,276,282,297,298,307,313,328,329,338,344]]
        return njogadores
    
    def player_x_l(self):
        nplayer_x = self.dataset.iloc[:,[18,49,80,111,142,173,204,235,266,297,328]]
        return nplayer_x

    def stamina_l(self):
        nstamina = self.dataset.iloc[:,[1,28,59,90,121,152,183,214,245,276,307,338]]
        return nstamina

    def player_xy_l(self):
        nplayer_xy = self.dataset.iloc[:,[1,10,11,18,19,49,50,80,81,111,112,142,143,173,174,204,205,235,236,266,267,297,298,328,329]]
        return nplayer_xy

    def zonadogol_r(self):
        nzonadogol = self.dataset[self.dataset['ball_x'] > -36.00].shape[0]
        return nzonadogol

    def gols_r(self):
        ngols = self.dataset[self.dataset['playmode'] == 'goal_r'].shape[0]
        return ngols

    def golsoponente_r(self):
        ngols = self.dataset[self.dataset['playmode'] == 'goal_l'].shape[0]
        return ngols

    def escanteio_r(self):
        nescanteio = self.dataset[self.dataset['playmode'] == 'corner_kick_r'].shape[0]
        return nescanteio

    def prafora_r(self):
        nprafora = self.dataset[self.dataset['playmode'] == 'goal_kick_r'].shape[0]
        return nprafora

    def jogadores_r(self):
        njogadores = self.dataset.iloc[:,[0,1,10,11,359,360,369,375,390,391,400,406,421,422,431,437,452,453,462,468,483,484,493,499,514,515,524,530,545,546,555,561,576,577,586,592,607,608,617,623,638,639,648,654,669,670,679,685]]
        return njogadores
    
    def player_x_r(self):
        nplayer_x = self.dataset.iloc[:,[359,390,421,452,483,514,545,576,607,638,669]]
        return nplayer_x

    def stamina_r(self):
        nstamina = self.dataset.iloc[:,[1,369,400,431,462,493,524,555,586,617,648,679]]
        return nstamina

    def player_xy_r(self):
        nplayer_xy = self.dataset.iloc[:,[1,10,11,359,360,390,391,421,422,452,453,483,484,514,515,545,546,576,577,607,608,638,639,669,670]]
        return nplayer_xy


#funções
def definicaodosatacantes_l (player_x,jogadoresrc):
    playerxcnames = player_x.columns
    atacantes = []
    index = 0
    atacantesid = [0]
    for column in playerxcnames:
        index +=1
        if jogadoresrc[jogadoresrc[str(column)] > 26].shape[0] > jogadoresrc[jogadoresrc[str(column)] < -26].shape[0]:
            atacantes.append(column)
            atacantesid.append(index)

def definicaodosatacantes_r (player_x,jogadoresrc):
    playerxcnames = player_x.columns
    atacantes = []
    index = 0
    atacantesid = [0]
    for column in playerxcnames:
        index +=1
        if jogadoresrc[jogadoresrc[str(column)] > -26].shape[0] > jogadoresrc[jogadoresrc[str(column)] < 26].shape[0]:
            atacantes.append(column)
            atacantesid.append(index)
    return atacantes, atacantesid

def datatempoofensivo_l(atacantes,dataset):
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
    tempototal = dataset['show_time'].shape[0] - tempoofensivo
    return tempoofensivo,temponaoofensivo,tempototal

def datatempoofensivo_r(atacantes,dataset):
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
    tempototal = dataset['show_time'].shape[0] - tempoofensivo
    return tempoofensivo,temponaoofensivo,tempototal


def jogadasofensivas_xy_l (player_xy,atacantes,goal_oponente):
    nao_atacantes = 25 - (len(atacantes)-1)*2
    lista_atcxy = list(range(nao_atacantes,25))
    lista_atcxy.append(0)
    lista_atcxy.append(1)
    lista_atcxy.append(2)
    lista_atcxy.sort()
    atacantes_xy = player_xy.iloc[:,lista_atcxy]
    posicoes_gol = atacantes_xy[atacantes_xy['playmode']=='goal_l']
    pgcolunas = posicoes_gol.columns
    for i in range(2,len(pgcolunas),2):
        posicoes_gol[pgcolunas[i]] = posicoes_gol[pgcolunas[i]]*-1

    def apagaduplicados(dataframe):
        aux = 0
        for i in dataframe.index:
            if i == aux+1:
                dataframe = dataframe.drop([i],axis=0)
            aux = i
        return dataframe

    posicoes_goltime = apagaduplicados(posicoes_gol)
    posicoes_goltime = posicoes_goltime.drop('playmode',axis=1)
    posicoesgoloponente = apagaduplicados(goal_oponente)
    posicoesgol_x = posicoes_goltime.iloc[:,list(range(0,len(posicoes_goltime.columns),2))]
    posicoesgol_y = posicoes_goltime.iloc[:,list(range(1,len(posicoes_goltime.columns),2))]
    return posicoesgol_x,posicoesgol_y,posicoesgoloponente, posicoes_goltime

def jogadasofensivas_xy_r (player_xy,atacantes,goal_oponente):
    nao_atacantes = 25 - (len(atacantes)-1)*2
    lista_atcxy = list(range(nao_atacantes,25))
    lista_atcxy.append(0)
    lista_atcxy.append(1)
    lista_atcxy.append(2)
    lista_atcxy.sort()
    atacantes_xy = player_xy.iloc[:,lista_atcxy]
    posicoes_gol = atacantes_xy[atacantes_xy['playmode']=='goal_r']
    pgcolunas = posicoes_gol.columns
    for i in range(2,len(pgcolunas),2):
        posicoes_gol[pgcolunas[i]] = posicoes_gol[pgcolunas[i]]*-1

    def apagaduplicados(dataframe):
        aux = 0
        for i in dataframe.index:
            if i == aux+1:
                dataframe = dataframe.drop([i],axis=0)
            aux = i
        return dataframe

    posicoes_goltime = apagaduplicados(posicoes_gol)
    posicoes_goltime = posicoes_goltime.drop('playmode',axis=1)
    posicoesgoloponente = apagaduplicados(goal_oponente)
    posicoesgol_x = posicoes_goltime.iloc[:,list(range(0,len(posicoes_goltime.columns),2))]
    posicoesgol_y = posicoes_goltime.iloc[:,list(range(1,len(posicoes_goltime.columns),2))]
    return posicoesgol_x,posicoesgol_y,posicoesgoloponente, posicoes_goltime

def graficostamina(stamina_players,atacantesid,posicoes_goltime,posicoesgoloponente):
    stamina_atacantes = stamina_players.iloc[:,atacantesid]
    graficosstamina = stamina_atacantes.plot(figsize=(13, 8), subplots=True)
    for axes in graficosstamina:
        axes.plot([posicoes_goltime.index,posicoes_goltime.index], [0, 8000], color="black")
        axes.plot([posicoesgoloponente.index,posicoesgoloponente.index], [0, 8000], color="red")
    plt.xlabel('Tempo de Jogo')
    plt.ylabel('Valor do atributo Stamina')
    plt.savefig('staminadosjogadores.png')


def graficostempoofensivo(tempoofensivo,temponaoofensivo,tempototal):
    seriesofensive = pd.Series([tempoofensivo,temponaoofensivo],index=['Tempo ofensivo','Tempo não ofensivo'], name='Período do Jogo')
    seriesofensive.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(10, 6))
    plt.title('Tempo ofensivo e tempo não ofensivo em lances com a bola no campo adversário')
    plt.savefig('tempoofensivozonadeataque.png')
    plt.cla()
    seriestempototal = pd.Series([tempototal,tempoofensivo],index=['Tempo não ofensivo', 'Tempo ofensivo'],name='Período do Jogo')
    seriestempototal.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(6, 6))
    plt.title('Tempo ofensivo em relação ao tempo total de jogo')
    plt.savefig('tempoofensivoxtotal.png')
    plt.cla()

def graficofinalizacoes (zonadogol, escanteio, prafora, gols):
    finalizacoes = pd.Series([zonadogol,escanteio,prafora,gols],index=['Linha do Ataque','Escanteio','Chute para fora','Gols'],name='Lances')
    finalizacoes.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(6, 6))
    plt.title('Finalizações e lances na linha do ataque')
    plt.savefig('finalizações.png')
    plt.cla()

def graficosposicaodegol (posicoesgol_x,posicoesgol_y):
    for i in range(len(posicoesgol_x.index)):
        plt.scatter(x=posicoesgol_x.iloc[i],y=posicoesgol_y.iloc[i],color=['red', 'green','green','green','green','green'])
        plt.axis([-56, 56, -35, 35])
        plt.title('Posição dos atacantes e da bola no lance do Gol')
        plt.xlabel('Coordenadas x do campo')
        plt.ylabel('Coordenadas y do campo')
        plt.savefig('posiçãodegol'+ str(i)+'.png')
        plt.cla()
