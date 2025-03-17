
def addEconomyInRound(rounds, ticks, wanted_ticks):
    df = ticks[ticks['tick'].isin(wanted_ticks)]
    for index, round in rounds.iterrows():
        subdf = df[df["total_rounds_played"] == round["round_num"] - 1]
        equip_value_ct = subdf[subdf['side'] == 'ct']['current_equip_value'].sum()
        equip_value_t = subdf[subdf['side'] == 't']['current_equip_value'].sum()
        rounds.loc[index, "CT_equip_value"] = equip_value_ct
        rounds.loc[index, "T_equip_value"] = equip_value_t
    
    return rounds