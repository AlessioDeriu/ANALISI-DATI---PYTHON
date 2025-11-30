import pandas as pd

# Dati originali
dati = {
    'Paese': ['SAINT LUCIA', 'CONGO', 'REUNION', 'NIGERIA', 'INDONESIA'],
    'Scali': [5, 3, 2, 4, 7],
    'Crew_Change': [None, None, None, None, None],
    'Porti': [
        'Castries, Vieux Fort',
        'Boma, Matadi',
        'Point des Galets, Reunion',
        'Apapa, Lagos',
        'Bahudopi, Balikpapan, Batam, Belawan, Jakarta, Palembang, Panjang, Surabaya'
    ]
}

# Creazione DataFrame
df = pd.DataFrame(dati)

def trova_info_paese(paese: str, dataframe: pd.DataFrame):
    
    #fornisce le informazioni di un paese dal DataFrame
    
    try:
        idx = dataframe[dataframe['Paese'] == paese].index[0]
        porti = dataframe.loc[idx, 'Porti']
        scali = dataframe.loc[idx, 'Scali']
        return{
            'posizione': idx,
            'porti': porti,
            'scali': scali
            
        }
    except IndexError:
        return None

#ex:

paese_cercato = 'SAINT LUCIA'
info = trova_info_paese(paese_cercato, df)

if info:
    print(f"Info su {paese_cercato}:")
    print(f" Posizione nel DataFrame: {info['posizione']}")
    print(f" Porti: {info['porti']}")
    print(f" Numero di scali: {info['scali']}")
else:
    print(f"{paese_cercato} non trovato nel DataFrame")



