# ANALISI_DATI-AGENZIA_MARITTIMA---PYTHON
Questo script Python crea un DataFrame con dati relativi a paesi, scali, cambi equipaggio e porti.
Permette di cercare informazioni specifiche su un paese, come:

-Porti
-Numero di scali
-Cambi equipaggio

In base alla frequenza di cambi equipaggio e operazioni nei porti da parte di un potenziale cliente, lo script può essere utile per stimare la mole di lavoro futura e pianificare un PDA (preventivo di costi) da proporre


Ingredients: Python 3 + pacchetto pandas

Modificare lo script per inserire i dati dei paesi e dei porti

Cercare le informazioni di un paese specifico cambiando la variabile:

paese_cercato = 'SAINT LUCIA'
info = trova_info_paese(paese_cercato, df)
Esempio di output
Info su SAINT LUCIA:
 Posizione nel DataFrame: 0
 Porti: Castries, Vieux Fort
 Numero di scali: 5
