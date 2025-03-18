# RoundsBrasil
 Análise se os times brasileiros perdem mais rounds contra eco ou semi armados que times internacionais

 ## Parâmetros Utilizados
 - Foram selecionados 9 times separados em 3 grupos:
    1. Brasil - **Furia**, **Pain** e **Mibr**
    2. Tier Brasil - Times com classificação parecidas com os times brasileiros - **Astralis**, **Heroic** e **3dmax**
    3. Tier S - **Vitality**, **Spirit**, **Navi**
 - Foram analisados 8 demos de partidas de cada time, podendo ser a partidas entre duas equipes analisadas
 - Parâmetro de economia no round:
    1. Round eco = Economia de inventório do time menor que 5100
    2. Round semi = Economia de inventório entre 5100 e 20000
    3. Round armado= Economia de inventório maior 20000
  
  ## Resultado
 Primeiramente gostaria de esclarecer que essa análise não tem como objetivo mostrar times melhores ou piores, foi feito um estudo de um aspecto específico do jogo e não tem como objetivo esclarecer o motivo dos times ganharem ou perderem os rounds.
 
 Dito isso, sendo bem sincero como um torcedor brasileiro sofredor eu espera grandes resultados sobre rounds armados contra ecos mas na prática o que se viu é que pouquíssimos armados perdem pra ecos, aparecendo apenas um caso em cada grupo

 ![alt text](https://github.com/AnalistaTerrorista/RoundsBrasil/blob/main/resultado.png)

Porém como o brasileiro precisa sofrer um pouco analisando a porcentagem de rounds armados ganhos contra ecos ou semis, vemos que os times brasileiros possuem uma eficiência mais baixa que os outros grupos:

 ![alt text](https://github.com/AnalistaTerrorista/RoundsBrasil/blob/main/graph/graph1.png)

Dentre os brasileiros parece que o MIBR possui uma efiência melhor mas ainda longe dos times internacionais:
 ![alt text](https://github.com/AnalistaTerrorista/RoundsBrasil/blob/main/graph/graph2.png)

 Eu pensei que a quantidade de rounds jogados poderia de alguma maneira prejudicar a análise dos times brasileiros, porém os times do **Tier Brasil** possuem uma quantidade de rounds maior que o **Tier S** porém com uma eficiência pior, dessa forma a eficiência e a quantidade total de rounds parece não ter uma corelação direta:
 ![alt text](https://github.com/AnalistaTerrorista/RoundsBrasil/blob/main/graph/graph3.png)

## Como executar a análise


## Como executar a análise
1. Baixe as demos e em uma pasta divida ela em subpastas no meu caso criei uma pasta para cada time
2. Crie um arquivo .env e adicione a variável demos_path com a pasta das demos
3. Execute o script main.py, o script extrai os mapas das demos e como resultado cria o arquivo **rouds_brasil.csv** com o resultado dos rounds
4. Execute o script create_chart.py para gerar os gráficos

## Referências
Demos analisadas:

     eternal-fire-vs-3dmax-m2-anubis.dem
     eternal-fire-vs-3dmax-m1-inferno.dem 
     falcons-vs-3dmax-m2-ancient.dem
     falcons-vs-3dmax-m3-dust2.dem 
     falcons-vs-3dmax-m1-inferno.dem
     liquid-vs-3dmax-m1-inferno.dem 
     liquid-vs-3dmax-m2-ancient.dem
     liquid-vs-3dmax-m3-anubis.dem 
     3dmax-vs-m80-m2-train.dem
     3dmax-vs-m80-m1-anubis.dem 
     3dmax-vs-tyloo-m1-ancient.dem
     3dmax-vs-tyloo-m2-inferno.dem 
     the-mongolz-vs-3dmax-m1-dust2.dem
     the-mongolz-vs-3dmax-m2-ancient.dem 
     3dmax-vs-saw-m1-nuke.dem
     3dmax-vs-saw-m2-dust2.dem 
     astralis-vs-big-m1-ancient.dem
     astralis-vs-big-m2-inferno.dem 
     astralis-vs-faze-m3-ancient.dem
     astralis-vs-faze-m1-mirage.dem 
     astralis-vs-faze-m2-inferno.dem
     falcons-vs-astralis-m1-ancient.dem 
     falcons-vs-astralis-m2-dust2.dem
     falcons-vs-astralis-m3-nuke.dem 
     mouz-vs-astralis-m2-nuke.dem
     mouz-vs-astralis-m3-ancient.dem 
     mouz-vs-astralis-m1-inferno.dem
     saw-vs-astralis-m1-nuke.dem 
     saw-vs-astralis-m2-inferno.dem
     the-mongolz-vs-astralis-m1-mirage.dem
     the-mongolz-vs-astralis-m2-inferno.dem 
     falcons-vs-furia-m1-train.dem
     falcons-vs-furia-m2-mirage.dem 
     falcons-vs-furia-m3-dust2.dem
     furia-vs-mibr-m3-inferno.dem 
     furia-vs-mibr-m1-anubis.dem
     furia-vs-mibr-m2-mirage.dem 
     liquid-vs-furia-m1-dust2.dem
     liquid-vs-furia-m2-anubis.dem 
     mouz-vs-furia-m1-train.dem
     mouz-vs-furia-m2-inferno.dem 
     mouz-vs-furia-m3-nuke.dem
     furia-vs-m80-m2-dust2.dem 
     furia-vs-m80-m3-anubis.dem
     furia-vs-m80-m1-mirage.dem 
     furia-vs-mibr-m2-nuke.dem
     furia-vs-nrg-m2-dust2.dem 
     furia-vs-nrg-m3-mirage.dem
     furia-vs-nrg-m1-train.dem 
     furia-vs-saw-m1-anubis.dem
     furia-vs-saw-m2-dust2.dem 
     furia-vs-saw-m3-inferno.dem
     heroic-vs-3dmax-m1-nuke.dem 
     heroic-vs-3dmax-m2-train.dem
     heroic-vs-nemiga-m1-dust2.dem 
     heroic-vs-nemiga-m2-mirage.dem
     heroic-vs-nemiga-m3-train.dem 
     heroic-vs-saw-m1-dust2.dem
     heroic-vs-saw-m2-train.dem 
     heroic-vs-saw-m3-ancient.dem
     big-vs-heroic-m2-ancient.dem
     big-vs-heroic-m1-mirage.dem 
     big-vs-heroic-m2-ancient.dem
     big-vs-heroic-m3-nuke.dem 
     heroic-vs-3dmax-m2-dust2.dem
     heroic-vs-3dmax-m3-ancient-p2.dem 
     heroic-vs-3dmax-m1-anubis.dem
     heroic-vs-astralis-m1-mirage.dem 
     heroic-vs-astralis-m2-nuke.dem
     heroic-vs-og-m1-dust2.dem 
     heroic-vs-og-m2-ancient.dem
     heroic-vs-og-m3-nuke.dem 
     eternal-fire-vs-mibr-m1-mirage.dem
     eternal-fire-vs-mibr-m2-inferno.dem
     gamerlegion-vs-mibr-m2-inferno.dem 
     gamerlegion-vs-mibr-m1-ancient.dem
     mibr-vs-nemiga-m1-anubis.dem 
     mibr-vs-nemiga-m2-inferno-p1.dem
     mibr-vs-nemiga-m3-mirage.dem 
     mibr-vs-tyloo-m1-inferno.dem
     mibr-vs-tyloo-m2-anubis.dem 
     vitality-vs-mibr-m1-anubis.dem
     vitality-vs-mibr-m2-inferno.dem 
     vitality-vs-mibr-m3-train.dem
     astralis-vs-mibr-m1-mirage.dem 
     astralis-vs-mibr-m2-inferno.dem
     astralis-vs-mibr-m3-nuke.dem 
     g2-vs-natus-vincere-m1-mirage.dem
     g2-vs-natus-vincere-m2-ancient.dem
     natus-vincere-vs-saw-m3-ancient.dem
     natus-vincere-vs-saw-m1-inferno.dem 
     natus-vincere-vs-saw-m2-nuke.dem
     natus-vincere-vs-tyloo-m1-inferno.dem
     natus-vincere-vs-tyloo-m2-mirage.dem
     natus-vincere-vs-tyloo-m3-ancient.dem
     the-mongolz-vs-natus-vincere-m2-ancient.dem
     the-mongolz-vs-natus-vincere-m1-mirage.dem
     eternal-fire-vs-pain-m1-nuke.dem 
     eternal-fire-vs-pain-m2-inferno.dem
     g2-vs-pain-m1-nuke.dem 
     g2-vs-pain-m2-inferno.dem
     gamerlegion-vs-pain-m1-nuke.dem 
     gamerlegion-vs-pain-m2-inferno.dem
     gamerlegion-vs-pain-m3-mirage.dem 
     pain-vs-natus-vincere-m2-mirage.dem
     pain-vs-natus-vincere-m1-train.dem 
     flyquest-vs-pain-m1-anubis.dem
     flyquest-vs-pain-m2-nuke.dem 
     flyquest-vs-pain-m3-inferno.dem
     pain-vs-lynn-vision-m2-nuke.dem 
     pain-vs-lynn-vision-m3-anubis.dem
     pain-vs-lynn-vision-m1-dust2.dem 
     pain-vs-m80-m1-anubis.dem
     pain-vs-m80-m2-mirage.dem 
     pain-vs-nemiga-m2-mirage.dem
     pain-vs-nemiga-m3-dust2.dem 
     pain-vs-nemiga-m1-train.dem
     spirit-vs-saw-m1-dust2.dem 
     spirit-vs-saw-m2-train.dem
     spirit-vs-the-mongolz-m1-anubis.dem
     spirit-vs-the-mongolz-m2-dust2.dem 
     spirit-vs-tyloo-m1-anubis-p2.dem
     spirit-vs-tyloo-m2-nuke.dem 
     gamerlegion-vs-spirit-m2-ancient-p2.dem
     gamerlegion-vs-spirit-m3-nuke-p3.dem
     gamerlegion-vs-spirit-m1-anubis-p1.dem
     gamerlegion-vs-spirit-m1-anubis-p2.dem
     gamerlegion-vs-spirit-m2-ancient-p1.dem
     liquid-vs-spirit-m1-nuke-p1.dem 
     liquid-vs-spirit-m1-nuke-p2.dem
     liquid-vs-spirit-m2-dust2.dem 
     natus-vincere-vs-spirit-m1-mirage.dem
     natus-vincere-vs-spirit-m2-dust2.dem
     virtus-pro-vs-spirit-m2-ancient.dem 
     virtus-pro-vs-spirit-m1-train.dem
     vitality-vs-spirit-m2-nuke.dem 
     vitality-vs-spirit-m3-mirage.dem
     vitality-vs-spirit-m1-dust2.dem 
     vitality-vs-3dmax-m1-train.dem
     vitality-vs-3dmax-m2-dust2.dem 
     vitality-vs-mouz-m1-inferno.dem
     vitality-vs-mouz-m2-dust2.dem 
     virtus-pro-vs-vitality-m1-anubis.dem
     virtus-pro-vs-vitality-m2-inferno.dem
     vitality-vs-3dmax-m1-inferno.dem 
     vitality-vs-3dmax-m2-nuke-p1.dem
     vitality-vs-faze-m2-anubis.dem 
     vitality-vs-faze-m3-dust2.dem
     vitality-vs-faze-m1-nuke.dem 
     vitality-vs-the-mongolz-m2-nuke.dem
     vitality-vs-the-mongolz-m1-mirage.dem
