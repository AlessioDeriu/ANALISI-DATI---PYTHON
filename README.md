# ANALISI-DATI---PYTHON
Questo script Python crea un DataFrame con dati di paesi, scali, crew change e porti.   Permette di cercare informazioni specifiche, ad esempio i porti, il numero di scali e cambi equipaggio performati in un paese, per un determinato periodo
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

# Posiz. riga "SAINT LUCIA"
try:
    idx_saint_lucia = df[df['Paese'] == 'SAINT LUCIA'].index[0]
    porto_saint_lucia = df.loc[idx_saint_lucia, 'Porti']
    scali_saint_lucia = df.loc[idx_saint_lucia, 'Scali']

    print("Posizione di SAINT LUCIA:", idx_saint_lucia)
    print("Porto corrispondente:", porto_saint_lucia)
    print("Numero di Scali:", scali_saint_lucia)
except IndexError:
    print("SAINT LUCIA non trovato nel DataFrame")
