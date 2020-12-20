import pandas as pd
import matplotlib.pyplot as plt
import singletonclasses as sc

arquivo = input()
timeanalisado = input()
datasethandle = pd.read_csv(arquivo)
dataset = datasethandle.drop_duplicates()
dados = sc.gameObject(dataset)

if (dados.time_l() == timeanalisado).bool():
    atacantes, atacantesid = sc.definicaodosatacantes_l(dados.player_x_l(),dados.jogadores_l())
    tempoofensivo,temponaoofensivo,tempototal = sc.datatempoofensivo_l(atacantes,dados.dataset)
    posicoesgol_x,posicoesgol_y,posicoesgoloponente, posicoes_goltime = sc.jogadasofensivas_xy_l(dados.player_xy_l(),atacantes,dados.golsoponente_l())
    sc.graficostempoofensivo(tempoofensivo,temponaoofensivo,tempototal)
    plt.cla()
    sc.graficosposicaodegol (posicoesgol_x,posicoesgol_y)
    plt.cla()
    sc.graficofinalizacoes (dados.zonadogol_l(), dados.escanteio_l(), dados.prafora_l(), dados.gols_l())
    plt.cla()
    sc.graficostamina(dados.stamina_l(),atacantesid,posicoes_goltime,posicoesgoloponente)
    plt.cla()
else:
    atacantes, atacantesid = sc.definicaodosatacantes_r(dados.player_x_r(),dados.jogadores_r())
    tempoofensivo,temponaoofensivo,tempototal = sc.datatempoofensivo_r(atacantes,dados.dataset())
    posicoesgol_x,posicoesgol_y,posicoesgoloponente, posicoes_goltime = sc.jogadasofensivas_xy_r (dados.player_xy_r(),atacantes,dados.golsoponente_r())
    sc.graficostamina(dados.stamina_r,atacantesid,posicoes_goltime,posicoesgoloponente)
    plt.cla()
    sc.graficostempoofensivo(tempoofensivo,temponaoofensivo,tempototal)
    plt.cla()
    sc.graficosposicaodegol (posicoesgol_x,posicoesgol_y)
    plt.cla()
    sc.graficofinalizacoes (dados.zonadogol_r(), dados.escanteio_r(), dados.prafora_r(), dados.gols_r())
    plt.cla()



