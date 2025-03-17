from awpy import Demo
import os
import rarfile
from round_win import *
from round_economy import *
from dotenv import load_dotenv

load_dotenv()
demos_path = os.environ.get('demos_path')
subfolders = [f.path for f in os.scandir(demos_path) if f.is_dir()]
for subfolder in subfolders:
    arqs = [f.path for f in os.scandir(subfolder) if 'falcons-vs-furia-bo3' in f.path]
    for arq in arqs:
        fileRar = rarfile.RarFile(arq)
        for file in fileRar.infolist():
            pathDemo = os.path.join(subfolder, file.filename)
            fileRar.extract(file.filename, subfolder)
            dem = Demo(pathDemo)
            dem.parse_events(['round_freeze_end'])
            dem.parse(player_props=["current_equip_value", "total_rounds_played", "team_clan_name", "side"])
            rounds_df = dem.rounds.to_pandas()
            ticks_df = dem.ticks.to_pandas()
            rounds_df = addTeamWinnerInRound(rounds_df, ticks_df)      
            
            wanted_ticks = dem.parse_events(['round_freeze_end'])['round_freeze_end']["tick"].to_list()
            ticks = dem.parse_ticks(player_props=["current_equip_value", "total_rounds_played", "team_clan_name", "side"]).to_pandas()
            rounds_df = addEconomyInRound(rounds_df, ticks_df, wanted_ticks)
            print(rounds_df)      
            
            os.remove(pathDemo)
