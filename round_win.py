
def addTeamWinnerInRound(rounds_df, ticks_df):
    for index, row in rounds_df.iterrows():
        freeze_end_tick = row["freeze_end"]
        winner = row["winner"]
        first_tick_df = ticks_df[ticks_df["tick"] == freeze_end_tick]
        ticks_t = first_tick_df.loc[first_tick_df['side'] == 't']
        ticks_ct = first_tick_df.loc[first_tick_df['side'] == 'ct']
        CT_team = ticks_ct.iloc[0]['team_clan_name']
        T_team = ticks_t.iloc[0]['team_clan_name']
        rounds_df.loc[index, "CT_team_clan_name"] = CT_team
        rounds_df.loc[index, "T_team_clan_name"] = T_team
        rounds_df.loc[index, "winner_clan_name"] = CT_team if winner == "ct" else T_team

    return rounds_df
    
