import pandas as pd
import matplotlib.pyplot as plt
import os

grupo1 = ["FURIA", "paiN Gaming", "MIBR"]
grupo2 = ["3DMAX", "Astralis", "HEROIC"]
grupo3 = ["Team Vitality", "Team Spirit", "Natus Vincere"]

df = pd.read_csv('rouds_brasil.csv')
df_result = pd.DataFrame(columns=['Grupo', 'Time','Rounds','Ecos Perdidos','Semis Perdidos','Armados Ganhos','% Armados Perdidos'])
for time in grupo1:
    tdf = df[(df.CT_team_clan_name == time) | (df.T_team_clan_name == time)]
    tdf_lose = tdf[((tdf.CT_team_clan_name == time) & (tdf.CT_equip_value == "armado") & (tdf.armado == "n") | (tdf.T_team_clan_name == time) & (tdf.T_equip_value == "armado") & (tdf.armado == "n"))]
    rounds_lose_eco = tdf_lose[(tdf.CT_equip_value == 'eco') | (tdf.T_equip_value == 'eco')]
    rounds_lose_semi= tdf_lose[(tdf.CT_equip_value == 'semi') | (tdf.T_equip_value == 'semi')]
    tdf_win = tdf[(((tdf.CT_team_clan_name == time) & (tdf.CT_equip_value == "armado") & (tdf.armado == "s")) | ((tdf.T_team_clan_name == time) & (tdf.T_equip_value == "armado") & (tdf.armado == "s")))]
    total_rounds = rounds_lose_eco.shape[0] + rounds_lose_semi.shape[0] + tdf_win.shape[0]
    new_row = {'Grupo': '1', 'Time': time, 'Rounds': total_rounds, 'Ecos Perdidos': rounds_lose_eco.shape[0], 'Semis Perdidos': rounds_lose_semi.shape[0], 'Armados Ganhos': tdf_win.shape[0], '% Armados Perdidos': (rounds_lose_eco.shape[0]+rounds_lose_semi.shape[0])/total_rounds}
    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)
   
for time in grupo2:
    tdf = df[(df.CT_team_clan_name == time) | (df.T_team_clan_name == time)]
    total_rounds = tdf.shape[0]
    tdf_lose = tdf[((tdf.CT_team_clan_name == time) & (tdf.CT_equip_value == "armado") & (tdf.armado == "n") | (tdf.T_team_clan_name == time) & (tdf.T_equip_value == "armado") & (tdf.armado == "n"))]
    rounds_lose_eco = tdf_lose[(tdf.CT_equip_value == 'eco') | (tdf.T_equip_value == 'eco')]
    rounds_lose_semi= tdf_lose[(tdf.CT_equip_value == 'semi') | (tdf.T_equip_value == 'semi')]
    tdf_win = tdf[((tdf.CT_team_clan_name == time) & (tdf.CT_equip_value == "armado") & (tdf.armado == "s") | (tdf.T_team_clan_name == time) & (tdf.T_equip_value == "armado") & (tdf.armado == "s"))]
    new_row = {'Grupo': '2', 'Time': time, 'Rounds': total_rounds, 'Ecos Perdidos': rounds_lose_eco.shape[0], 'Semis Perdidos': rounds_lose_semi.shape[0], 'Armados Ganhos': tdf_win.shape[0], '% Armados Perdidos': (rounds_lose_eco.shape[0]+rounds_lose_semi.shape[0])/total_rounds}
    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)
   
for time in grupo3:
    tdf = df[(df.CT_team_clan_name == time) | (df.T_team_clan_name == time)]
    total_rounds = tdf.shape[0]
    tdf_lose = tdf[((tdf.CT_team_clan_name == time) & (tdf.CT_equip_value == "armado") & (tdf.armado == "n") | (tdf.T_team_clan_name == time) & (tdf.T_equip_value == "armado") & (tdf.armado == "n"))]
    rounds_lose_eco = tdf_lose[(tdf.CT_equip_value == 'eco') | (tdf.T_equip_value == 'eco')]
    rounds_lose_semi= tdf_lose[(tdf.CT_equip_value == 'semi') | (tdf.T_equip_value == 'semi')]
    tdf_win = tdf[((tdf.CT_team_clan_name == time) & (tdf.CT_equip_value == "armado") & (tdf.armado == "s") | (tdf.T_team_clan_name == time) & (tdf.T_equip_value == "armado") & (tdf.armado == "s"))]
    new_row = {'Grupo': '3', 'Time': time, 'Rounds': total_rounds, 'Ecos Perdidos': rounds_lose_eco.shape[0], 'Semis Perdidos': rounds_lose_semi.shape[0], 'Armados Ganhos': tdf_win.shape[0], '% Armados Perdidos': (rounds_lose_eco.shape[0]+rounds_lose_semi.shape[0])/total_rounds}
    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)

grupos = ['Brasil', 'Tier Brasil', 'Tier S']
lose_arm_grupo1 = df_result[(df_result.Grupo == '1')]["% Armados Perdidos"].median() * 100
lose_arm_grupo2 = df_result[(df_result.Grupo == '2')]["% Armados Perdidos"].median() * 100
lose_arm_grupo3 = df_result[(df_result.Grupo == '3')]["% Armados Perdidos"].median() * 100
loses = [lose_arm_grupo1, lose_arm_grupo2, lose_arm_grupo3]

current_directory_path = os.getcwd()
plot_path = os.path.join(current_directory_path, "graph")
plot_name = 'result.png'
                         
fig, ax = plt.subplots()
bar_container = ax.bar(grupos, loses)
ax.set(ylabel='%', title='Percentual de Rounds Armados perdidos para Ecos e Semis por grupos')
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.savefig(os.path.join(plot_path, "graph1.png"))

lose_furia = df_result[df_result.Time == 'FURIA']["% Armados Perdidos"].median() * 100
lose_pain = df_result[(df_result.Time == 'paiN Gaming')]["% Armados Perdidos"].median() * 100
lose_mibr = df_result[df_result.Time == 'MIBR']["% Armados Perdidos"].median() * 100

lose_br = [lose_furia, lose_pain, lose_mibr]
fig, ax = plt.subplots()
bar_container = ax.bar(grupo1, lose_br)
ax.set(ylabel='%', title='Percentual de Rounds Armados perdidos para Ecos e Semis - Brasil')
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.savefig(os.path.join(plot_path, "graph2.png"))

print(df_result)

total_round_furia = df_result[df_result.Time == 'FURIA']["Rounds"].median()
total_round_pain = df_result[(df_result.Time == 'paiN Gaming')]["Rounds"].median()
total_round_mibr = df_result[df_result.Time == 'MIBR']["Rounds"].median()
total_round_3dmax = df_result[df_result.Time == '3DMAX']["Rounds"].median()
total_round_astralis = df_result[(df_result.Time == 'Astralis')]["Rounds"].median()
total_round_heroic = df_result[df_result.Time == 'HEROIC']["Rounds"].median()
total_round_vitality = df_result[df_result.Time == 'Team Vitality']["Rounds"].median()
total_round_spirit = df_result[(df_result.Time == 'Team Spirit')]["Rounds"].median()
total_round_navi = df_result[df_result.Time == 'Natus Vincere']["Rounds"].median()

times = ['FURIA', 'paiN Gaming', 'MIBR', '3DMAX', 'Astralis', 'HEROIC', 'Team Vitality', 'Team Spirit', 'Natus Vincere']
rounds = [total_round_furia, total_round_pain, total_round_mibr, total_round_3dmax, total_round_astralis, total_round_heroic, total_round_vitality, total_round_spirit, total_round_navi]
fig, ax = plt.subplots(figsize=(12, 8))
bar_container = ax.bar(times, rounds)
ax.set(title='Total de rounds armados contra ecos e semis')
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.savefig(os.path.join(plot_path, "graph3.png"))