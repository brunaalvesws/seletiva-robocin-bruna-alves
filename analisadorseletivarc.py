import pandas as pd
import matplotlib.pyplot as plt
import singletonclasses as sc

arquivo = input()
timeanalisado = input()
datasethandle = pd.read_csv(arquivo)
dataset = datasethandle.drop_duplicates()
#inicialização de classes
game_object = sc.gameObject()
classe_time_l = sc.time_l(dataset)
game_object.set_time_l(classe_time_l)
timeesquerda = game_object.get_time_l()

if (timeesquerda.ntime == timeanalisado).bool():
    #inicialização classes esquerda
    classe_zonadogol_l = sc.zonadogol_l(dataset)
    game_object.set_zonadogol_l(classe_zonadogol_l)
    zonadogolesquerda = game_object.get_zonadogol_l()

    classe_gols_l = sc.gols_l(dataset)
    game_object.set_gols_l(classe_gols_l)
    golsesquerda = game_object.get_gols_l()

    classe_golsop_l = sc.golsoponente_l(dataset)
    game_object.set_golsoponente_l(classe_golsop_l)
    golsopesquerda = game_object.get_golsoponente_l()

    classe_escanteio_l = sc.escanteio_l(dataset)
    game_object.set_escanteio_l(classe_escanteio_l)
    escanteioesquerda = game_object.get_escanteio_l()

    classe_prafora_l = sc.prafora_l(dataset)
    game_object.set_prafora_l(classe_prafora_l)
    praforaesquerda = game_object.get_prafora_l()

    classe_jogadores_l = sc.jogadores_l(dataset)
    game_object.set_jogadores_l(classe_jogadores_l)
    jogadoresesquerda = game_object.get_jogadores_l()

    classe_player_x_l = sc.player_x_l(dataset)
    game_object.set_player_x_l(classe_player_x_l)
    player_xesquerda = game_object.get_player_x_l()

    classe_stamina_l = sc.stamina_l(dataset)
    game_object.set_stamina_l(classe_stamina_l)
    staminaesquerda = game_object.get_stamina_l()

    classe_player_xy_l = sc.player_xy_l(dataset)
    game_object.set_player_xy_l(classe_player_xy_l)
    player_xyesquerda = game_object.get_player_xy_l()

    #funções
    atacantes, atacantesid = sc.definicaodosatacantes_l(player_xesquerda.nplayer_x,jogadoresesquerda.njogadores)
    tempoofensivo,temponaoofensivo,tempototal = sc.datatempoofensivo_l(atacantes,dataset)
    posicoesgol_x,posicoesgol_y,posicoesgoloponente, posicoes_goltime = sc.jogadasofensivas_xy_l(player_xyesquerda.nplayer_xy,atacantes,golsopesquerda.ngols)
    #plotar os gráficos
    sc.graficostempoofensivo(tempoofensivo,temponaoofensivo,tempototal)
    plt.cla()
    sc.graficosposicaodegol (posicoesgol_x,posicoesgol_y)
    plt.cla()
    sc.graficofinalizacoes (zonadogolesquerda.nzonadogol, escanteioesquerda.nescanteio, praforaesquerda.nprafora, golsesquerda.ngols)
    plt.cla()
    sc.graficostamina(staminaesquerda.nstamina,atacantesid,posicoes_goltime,posicoesgoloponente)
    plt.cla()
else:
    #inicialização classes direita
    classe_zonadogol_r = sc.zonadogol_r(dataset)
    game_object.set_zonadogol_r(classe_zonadogol_r)
    zonadogoldireita = game_object.get_zonadogol_r()

    classe_gols_r = sc.gols_r(dataset)
    game_object.set_gols_r(classe_gols_r)
    golsdireita = game_object.get_gols_r()

    classe_golsop_r = sc.golsoponente_r(dataset)
    game_object.set_golsoponente_r(classe_golsop_r)
    golsopdireita = game_object.get_golsoponente_r()

    classe_escanteio_r = sc.escanteio_r(dataset)
    game_object.set_escanteio_r(classe_escanteio_r)
    escanteiodireita = game_object.get_escanteio_r()

    classe_prafora_r = sc.prafora_r(dataset)
    game_object.set_prafora_r(classe_prafora_r)
    praforadireita = game_object.get_prafora_r()

    classe_jogadores_r = sc.jogadores_r(dataset)
    game_object.set_jogadores_r(classe_jogadores_r)
    jogadoresdireita = game_object.get_jogadores_r()

    classe_player_x_r = sc.player_x_r(dataset)
    game_object.set_player_x_r(classe_player_x_r)
    player_xdireita = game_object.get_player_x_r()

    classe_stamina_r = sc.stamina_r(dataset)
    game_object.set_stamina_r(classe_stamina_r)
    staminadireita = game_object.get_stamina_r()

    classe_player_xy_r = sc.player_xy_r(dataset)
    game_object.set_player_xy_r(classe_player_xy_r)
    player_xydireita = game_object.get_player_xy_r()

    #funções
    atacantes, atacantesid = sc.definicaodosatacantes_r(player_xdireita.nplayer_x, jogadoresdireita.njogadores)
    tempoofensivo,temponaoofensivo,tempototal = sc.datatempoofensivo_r(atacantes,dataset)
    posicoesgol_x,posicoesgol_y,posicoesgoloponente, posicoes_goltime = sc.jogadasofensivas_xy_r (player_xydireita.nplayer_xy,atacantes,golsopdireita.ngols)
    #plotar os gráficos
    sc.graficostempoofensivo(tempoofensivo,temponaoofensivo,tempototal)
    plt.cla()
    sc.graficosposicaodegol (posicoesgol_x,posicoesgol_y)
    plt.cla()
    sc.graficofinalizacoes (zonadogoldireita.nzonadogol, escanteiodireita.nescanteio, praforadireita.nprafora, golsdireita.ngols)
    plt.cla()
    sc.graficostamina(staminadireita.nstamina,atacantesid,posicoes_goltime,posicoesgoloponente)
    plt.cla()
