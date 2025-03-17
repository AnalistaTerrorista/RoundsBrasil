
def addEconomyInRound(rounds, ticks, wanted_ticks):
    eco_ct = 5100
    eco_t = 5100
    semi_ct = 20000
    semi_t = 20000
    df = ticks[ticks['tick'].isin(wanted_ticks)]
    for index, round in rounds.iterrows():
        subdf = df[df["total_rounds_played"] == round["round_num"] - 1]
        equip_value_ct = subdf[subdf['side'] == 'ct']['current_equip_value'].sum()
        equip_value_t = subdf[subdf['side'] == 't']['current_equip_value'].sum()
        rounds.loc[index, "CT_equip_value"] = 'eco' if equip_value_ct < eco_ct else 'semi' if equip_value_ct < semi_ct else 'armado'
        rounds.loc[index, "T_equip_value"] = 'eco' if equip_value_t < eco_t else 'semi' if equip_value_t < semi_t else 'armado'
    
    return rounds