# Lee la tabla de expedientes y exporta los delitos únicos (por id)
# a un .xls en el mismo directorio
# > pip install pandas xlwt

import pandas as pd

csv_path = 'penal_df.csv'

df = pd.read_csv(csv_path)
# reportar nombres de columnas
#print(df.columns.values)

# seleccionar las columnas que nos interesan
dfOju = df.loc[:, 'oju_id':'oju_descr']
# reportar el tamaño agrupado por id
#print(dfOju.groupby(by='oju_id').first().shape)
# reportar el tamaño agrupado por descripción
#print(dfOju.groupby(by='oju_descr').first().shape)

# agrupar por id (únicos)
dfOjuUniq = dfOju.groupby(by='oju_id').first()
print(dfOjuUniq)

# exportar a xls (requiere el módulo xlwt)
dfOjuUniq.to_excel('delitos_id_unique.xls')

