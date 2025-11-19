import pandas as pd
df = pd.read_csv('schueler.csv')
df = df.sort_values(by=['Stufe', 'Klasse','Nachname','Vorname'], ascending = [True, True, True, True], ignore_index=True)  
print(df)