import pandas as pd

def load_ridership(path):
    df = pd.read_csv(path)
    df.drop([1222104, 1222105, 1222106])
    agg = df.groupby(['stop_id', 'service_date'])['gated_entries'].sum().reset_index()
    agg = agg.groupby('stop_id')['gated_entries'].agg(
        ['mean','sum','count']).reset_index()
    agg = agg.rename(columns={'mean':'entries_mean','sum':'entries_total','count':'n_observations'})
    return agg
agg = load_ridership('MBTA_Gated_Station_Entries.csv')
agg.to_csv("gated_entries_by_day.csv", index=False)