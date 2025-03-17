from awpy import Demo
from round_win import *
from round_economy import *
import pandas as pd

def calculeMatch(pathDemo, jogo):
    parse_player_props = ["current_equip_value", "total_rounds_played", "team_clan_name", "side"]
    columns_csv = ["jogo", "round_num", "winner", "CT_team_clan_name", "T_team_clan_name", "winner_clan_name", "CT_equip_value", "T_equip_value", "armado"]
    dem = Demo(pathDemo)
    dem.parse_events(['round_freeze_end'])
    dem.parse(player_props=parse_player_props)
    rounds_df = dem.rounds.to_pandas()
    ticks_df = dem.ticks.to_pandas()
    rounds_df = addTeamWinnerInRound(rounds_df, ticks_df)      
    
    wanted_ticks = dem.parse_events(['round_freeze_end'])['round_freeze_end']["tick"].to_list()
    rounds_df = addEconomyInRound(rounds_df, ticks_df, wanted_ticks)
    
    rounds_ct_win = rounds_df[(rounds_df.winner == 'ct') & (rounds_df.T_equip_value == 'armado') & (rounds_df.CT_equip_value != 'armado')]
    rounds_ct_win["jogo"] = jogo
    rounds_ct_win["armado"] = "n"
    df = rounds_ct_win[columns_csv]
    rounds_ct_win_arm = rounds_df[(rounds_df.winner == 'ct') & (rounds_df.T_equip_value != 'armado') & (rounds_df.CT_equip_value == 'armado')]
    rounds_ct_win_arm["jogo"] = jogo
    rounds_ct_win_arm["armado"] = "s"
    df = pd.concat([df, rounds_ct_win_arm[columns_csv]], ignore_index=True)
    
    rounds_t_win = rounds_df[(rounds_df.winner == 't') & (rounds_df.CT_equip_value == 'armado') & (rounds_df.T_equip_value != 'armado')]
    rounds_t_win["jogo"] = jogo
    rounds_t_win["armado"] = "n"
    df = pd.concat([df, rounds_t_win[columns_csv]], ignore_index=True)
    rounds_t_win_arm = rounds_df[(rounds_df.winner == 't') & (rounds_df.CT_equip_value != 'armado') & (rounds_df.T_equip_value == 'armado')]
    rounds_t_win_arm["jogo"] = jogo
    rounds_t_win_arm["armado"] = "s"
    df = pd.concat([df, rounds_t_win_arm[columns_csv]], ignore_index=True)
    
    return df