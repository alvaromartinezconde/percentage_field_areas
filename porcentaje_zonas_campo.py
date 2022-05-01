import pandas as pd
import matplotlib.pyplot as plt
import matplotlib; matplotlib.style.use('ggplot')

# To use google drive:

# from google.colab import drive
# drive.mount('/content/drive')


ruta_jugadores = "inputs/eventos_2020_2021.csv"
df = pd.read_csv(ruta_jugadores)


dfmatch = (
    
    ((df['team']=='Atletico de Madrid') | (df['team']=='Cadiz CF')) & ((df['year']==2021) & (df['month']==1) & (df['day']==31)))


df_match = df[dfmatch]


zona_cadiz = ((df_match['team']=='Cadiz CF'))

jug_cadiz = df_match[zona_cadiz].loc[:, ['x']]


# ZONE 1 (0 to 17 ); ZONE 2 (18 to 50); ZONE 3 (51 to 83); ZONE 4 (84 to 100)

zona1_cad = (jug_cadiz['x']<=17)
zona1_cadiz = jug_cadiz[zona1_cad].count()
Cadiz_zona1 = zona1_cadiz/874

zona2_cad = ((jug_cadiz['x']>17) & (jug_cadiz['x']<=50))
zona2_cadiz = jug_cadiz[zona2_cad].count()
Cadiz_zona2 = zona2_cadiz/874

zona3_cad = ((jug_cadiz['x']>50) & (jug_cadiz['x']<=83))
zona3_cadiz = jug_cadiz[zona3_cad].count()
Cadiz_zona3 = zona3_cadiz/874

zona4_cad = jug_cadiz['x']>83
zona4_cadiz = jug_cadiz[zona4_cad].count()
Cadiz_zona4 = zona4_cadiz/874

Porc_zonas = Cadiz_zona1.x * 100, Cadiz_zona2.x * 100, Cadiz_zona3.x * 100, Cadiz_zona4.x * 100

Porc_zonas
