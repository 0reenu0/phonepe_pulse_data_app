
def preprocess_state_name(df):

    df['State']=df['State'].apply(lambda a: " ".join([k.capitalize() if k.lower() != 'and' else k for k in a.split('-')]))
    df['State']=df['State'].apply(lambda a: " ".join([k.replace('-',' ') for k in a.split()]))

    #mask=(df['Year']==2018)
    #df2=df[mask]
    #mask1=df2['Quarter']==1
    #df2=df2[mask1]
    #mask2=df2['Transaction_type'].isin(['Peer-to-peer payments']) 
    #df3=df2[mask2]

    return df

def convert_to_str_tuple(series):
    tuples = []
    for row in series.itertuples():
    # Each row is a namedtuple with the column values
    # Extract the column value as a string
        tuples.append(str(row.Year))
    tuple_of_strings = tuple(tuples)
    return tuple_of_strings