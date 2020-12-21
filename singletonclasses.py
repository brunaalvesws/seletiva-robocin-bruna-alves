import pandas as pd
import matplotlib.pyplot as plt

#singleton
class gameObject:

    _instance = None

    def __init__(self):
        self.time_l = None
        self.zonadogol_l = None
        self.gols_l = None
        self.golsoponente_l = None
        self.escanteio_l = None
        self.prafora_l = None
        self.jogadores_l = None
        self.player_x_l = None
        self.stamina_l = None
        self.player_xy_l = None
        self.zonadogol_r = None
        self.gols_r = None
        self.golsoponente_r = None
        self.escanteio_r = None
        self.prafora_r = None
        self.jogadores_r = None
        self.player_x_r = None
        self.stamina_r = None
        self.player_xy_r = None
    
    def set_time_l(self,time):
        self.time_l = time

    def get_time_l(self):
        return self.time_l

    def set_zonadogol_l(self,zonadogol):
        self.zonadogol_l = zonadogol

    def get_zonadogol_l(self):
        return self.zonadogol_l

    def set_gols_l(self,gols):
        self.gols_l = gols

    def get_gols_l(self):
        return self.gols_l

    def set_golsoponente_l(self,golsoponente):
        self.golsoponente_l = golsoponente
        
    def get_golsoponente_l(self):
        return self.golsoponente_l

    def set_escanteio_l(self,escanteio):
        self.escanteio_l = escanteio
        
    def get_escanteio_l(self):
        return self.escanteio_l

    def set_prafora_l(self,prafora):
        self.prafora_l = prafora
        
    def get_prafora_l(self):
        return self.prafora_l

    def set_jogadores_l(self,jogadores):
        self.jogadores_l = jogadores
        
    def get_jogadores_l(self):
        return self.jogadores_l

    def set_player_x_l(self,player_x):
        self.player_x_l = player_x
        
    def get_player_x_l(self):
        return self.player_x_l

    def set_stamina_l(self,stamina):
        self.stamina_l = stamina
        
    def get_stamina_l(self):
        return self.stamina_l

    def set_player_xy_l(self,player_xy):
        self.player_xy_l = player_xy
        
    def get_player_xy_l(self):
        return self.player_xy_l

    def set_zonadogol_r(self,zonadogol):
        self.zonadogol_r = zonadogol

    def get_zonadogol_r(self):
        return self.zonadogol_r

    def set_gols_r(self,gols):
        self.gols_r = gols

    def get_gols_r(self):
        return self.gols_r

    def set_golsoponente_r(self,golsoponente):
        self.golsoponente_r = golsoponente
        
    def get_golsoponente_r(self):
        return self.golsoponente_r

    def set_escanteio_r(self,escanteio):
        self.escanteio_r = escanteio
        
    def get_escanteio_r(self):
        return self.escanteio_r

    def set_prafora_r(self,prafora):
        self.prafora_r = prafora
        
    def get_prafora_r(self):
        return self.prafora_r

    def set_jogadores_r(self,jogadores):
        self.jogadores_r = jogadores
        
    def get_jogadores_r(self):
        return self.jogadores_r

    def set_player_x_r(self,player_x):
        self.player_x_r = player_x
        
    def get_player_x_r(self):
        return self.player_x_r

    def set_stamina_r(self,stamina):
        self.stamina_r = stamina
        
    def get_stamina_r(self):
        return self.stamina_r

    def set_player_xy_r(self,player_xy):
        self.player_xy_r = player_xy
        
    def get_player_xy_r(self):
        return self.player_xy_r

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

#subclasses
class time_l:
    def __init__(self, dataframe):
        self.ntime = dataframe.iloc[[0],[2]]
        
class zonadogol_l:
    def __init__(self, dataframe):
        self.nzonadogol = dataframe[dataframe['ball_x'] > 36.00].shape[0]

class gols_l:
    def __init__(self, dataframe):
        self.ngols = dataframe[dataframe['playmode'] == 'goal_l'].shape[0]

class golsoponente_l:
    def __init__(self, dataframe):
        self.ngols = dataframe[dataframe['playmode'] == 'goal_r']

class escanteio_l:
    def __init__(self, dataframe):
        self.nescanteio = dataframe[dataframe['playmode'] == 'corner_kick_l'].shape[0]

class prafora_l:
    def __init__(self, dataframe):
        self.nprafora = dataframe[dataframe['playmode'] == 'goal_kick_l'].shape[0]

class jogadores_l:
    def __init__(self, dataframe):
        self.njogadores = dataframe.iloc[:,[0,1,10,11,18,19,28,34,49,50,59,65,80,81,90,96,111,112,121,127,142,143,152,158,173,174,183,189,204,205,214,220,235,236,245,251,266,267,276,282,297,298,307,313,328,329,338,344]]
    
class player_x_l:
    def __init__(self, dataframe):
        self.nplayer_x = dataframe.iloc[:,[18,49,80,111,142,173,204,235,266,297,328]]

class stamina_l:
    def __init__(self, dataframe):
        self.nstamina = dataframe.iloc[:,[1,28,59,90,121,152,183,214,245,276,307,338]]

class player_xy_l:
    def __init__(self, dataframe):
        self.nplayer_xy = dataframe.iloc[:,[1,10,11,18,19,49,50,80,81,111,112,142,143,173,174,204,205,235,236,266,267,297,298,328,329]]

class zonadogol_r:
    def __init__(self, dataframe):
        self.nzonadogol = dataframe[dataframe['ball_x'] > -36.00].shape[0]

class gols_r:
    def __init__(self, dataframe):
        self.ngols = dataframe[dataframe['playmode'] == 'goal_r'].shape[0]

class golsoponente_r:
    def __init__(self, dataframe):
        self.ngols = dataframe[dataframe['playmode'] == 'goal_l']

class escanteio_r:
    def __init__(self, dataframe):
        self.nescanteio = dataframe[dataframe['playmode'] == 'corner_kick_r'].shape[0]

class prafora_r:
    def __init__(self, dataframe):
        self.nprafora = dataframe[dataframe['playmode'] == 'goal_kick_r'].shape[0]

class jogadores_r:
    def __init__(self, dataframe):
        self.njogadores = dataframe.iloc[:,[0,1,10,11,359,360,369,375,390,391,400,406,421,422,431,437,452,453,462,468,483,484,493,499,514,515,524,530,545,546,555,561,576,577,586,592,607,608,617,623,638,639,648,654,669,670,679,685]]
    
class player_x_r:
    def __init__(self, dataframe):
        self.nplayer_x = dataframe.iloc[:,[359,390,421,452,483,514,545,576,607,638,669]]

class stamina_r:
    def __init__(self, dataframe):
        self.nstamina = dataframe.iloc[:,[1,369,400,431,462,493,524,555,586,617,648,679]]

class player_xy_r:
    def __init__(self, dataframe):
        self.nplayer_xy = dataframe.iloc[:,[1,10,11,359,360,390,391,421,422,452,453,483,484,514,515,545,546,576,577,607,608,638,639,669,670]]


#funções de definição
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
    return atacantes, atacantesid

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

    def apagaduplicados(tabela):
        aux = 0
        for i in tabela.index:
            if i == aux+1:
                tabela = tabela.drop([i],axis=0)
            aux = i
        return tabela

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


#funções de plotagem
def graficostamina(stamina_players,atacantesid,posicoes_goltime,posicoesgoloponente):
    stamina_atacantes = stamina_players.iloc[:,atacantesid]
    graficosstamina = stamina_atacantes.plot(figsize=(13, 8), subplots=True)
    if posicoes_goltime.shape[0] != 0:
        for axes in graficosstamina:
            axes.plot([posicoes_goltime.index,posicoes_goltime.index], [0, 8000], color="black")
    if posicoesgoloponente.shape[0] != 0:
        for axes in graficosstamina:
            axes.plot([posicoesgoloponente.index,posicoesgoloponente.index], [0, 8000], color="red")
    plt.xlabel('Tempo de Jogo')
    plt.ylabel('Valor do atributo Stamina')
    plt.savefig('staminadosjogadores.png')
    plt.cla()


def graficostempoofensivo(tempoofensivo,temponaoofensivo,tempototal):
    seriesofensive = pd.Series([tempoofensivo,temponaoofensivo],index=['Tempo ofensivo','Tempo não ofensivo'], name='Período do Jogo')
    seriesofensive.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(10, 8))
    plt.title('Tempo ofensivo e tempo não ofensivo em lances com a bola no campo adversário')
    plt.savefig('tempoofensivozonadeataque.png')
    plt.cla()
    seriestempototal = pd.Series([tempototal,tempoofensivo],index=['Tempo não ofensivo', 'Tempo ofensivo'],name='Período do Jogo')
    seriestempototal.plot.pie(colors=['#038d05', '#117401', '#005813', '#00400e'],figsize=(10, 8))
    plt.title('Tempo ofensivo em relação ao tempo total de jogo')
    plt.savefig('tempoofensivoxtotal.png')
    plt.cla()


def graficofinalizacoes (zonadogol, escanteio, prafora, gols):
    listalances = [zonadogol]
    nomes = ['Linha do Ataque']
    cores = ['#038d05']
    if gols != 0:
        listalances.append(gols)
        nomes.append('Gols')
        cores.append('#117401')
    if escanteio != 0:
        listalances.append(escanteio)
        nomes.append('Escanteio')
        cores.append('#005813')
    if prafora != 0:
        listalances.append(prafora)
        nomes.append('Chute para linha de fundo')
        cores.append('#00400e')
    finalizacoes = pd.Series(listalances,index=nomes,name='Lances')
    finalizacoes.plot.pie(colors=cores,figsize=(12, 8))
    plt.title('Finalizações e lances na linha do ataque')
    plt.savefig('finalizações.png')
    plt.cla()

    
def graficosposicaodegol (posicoesgol_x,posicoesgol_y):
    cores = ['red']
    for i in range(len(posicoesgol_x.columns)-1):
        cores.append('green')
    for i in range(len(posicoesgol_x.index)):
        plt.scatter(x=posicoesgol_x.iloc[i],y=posicoesgol_y.iloc[i],color=cores)
        plt.axis([-56, 56, -35, 35])
        plt.title('Posição dos atacantes e da bola no lance do Gol')
        plt.xlabel('Coordenadas x do campo')
        plt.ylabel('Coordenadas y do campo')
        plt.savefig('posiçãodegol'+ str(i)+'.png')
        plt.cla()
