from pprint import pprint
import math
from random import randint
import time
import sys
#import random
#my_list = ['A'] * 5 + ['B'] * 5 + ['C'] * 90
#random.choice(my_list)

#pip install pandas numpy matplotlib
import pandas as pd
import numpy
import matplotlib.pyplot as plt

# por ahora hacemos que cada gravedad pese igual que su número
# a cambiar!
gravedad_pesos = {i:i for i in range(1, 9)}
print(f'Pesos de gravedades de delitos: {gravedad_pesos}')

juzgadosTacuari = [
	1, 2, 3, 5, 7, 8, 10,
	11, 14, 16, 17, 18, 19,
	20, 21, 22, 25, 26
]
juzgadosBeruti = []
for i in range(1, 32):
	if i not in juzgadosTacuari:
		juzgadosBeruti.append(i)
print('Juzgados Tacuarí', juzgadosTacuari, '\nJuazgados Beruti', juzgadosBeruti)

delitos_gravedad_path = 'Tipos de delitos por complejidad - tipos-delitos.csv'
delitos_gravedad = {}
df = pd.read_csv(delitos_gravedad_path)
for index, row in df.iterrows():
	gravedad_id = row['ID']
	#print(gravedad_id, row['oju_id'])
	if not gravedad_id or gravedad_id == '?' or math.isnan(float(gravedad_id)):
		continue
	if row['oju_id'] not in delitos_gravedad:
		delitos_gravedad[int(row['oju_id'])] = int(gravedad_id)
pprint(delitos_gravedad)
sys.exit()

class Juazgado:
	def __init__(self, numero):
		self.numero = numero
		self.estacuari = numero in juzgadosTacuari
		self.gravedad_acumulada = 1.0
		self.causas_asignadas = 0
juzgados = []
for i in range(1, 32):
	juzgados.append(Juazgado(i))

juzgados_asignados = []
expedientes_path = 'penal_df.csv'
df = pd.read_csv(expedientes_path)


start = time.time()
for index, row in df.iterrows():
	delito_id = row['oju_id']
	if not delito_id:
		juzgados_asignados.append(None)
		continue
	delito_id = int(delito_id)
	if not delito_id in delitos_gravedad:
		juzgados_asignados.append(None)
		continue
	# traemos el peso del delito del expediente actual
	gravedad_delito = delitos_gravedad[delito_id]
	gravedad_peso = gravedad_pesos[gravedad_delito]
	
	# ordenamos los juzgados con menos gravedad acumulada
	'''juzgados.sort(key=lambda x: x.gravedad_acumulada)
	juzgados_sorteo = [juzgados[0]]
	for juz in juzgados:
		if juz.gravedad_acumulada == juzgados[0].gravedad_acumulada:
			juzgados_sorteo.append(juz)
		else:
			break
	sorteo = randint(1, 31)'''
	
	total_gravedades = sum(juz.gravedad_acumulada for juz in juzgados)
	pesos = [1-juz.gravedad_acumulada/total_gravedades for juz in juzgados]
	total_pesos = sum(pesos)
	pesos_normalizados = [peso/total_pesos for peso in pesos]
	#print(total_gravedades, pesos, pesos_normalizados)
	
	juzgado_sorteado = numpy.random.choice(juzgados, p=pesos_normalizados)
	juzgados_asignados.append(juzgado_sorteado.numero)
	juzgado_sorteado.gravedad_acumulada += gravedad_peso
	juzgado_sorteado.causas_asignadas += 1

end = time.time()
print(f'Tiempo de ejecución de algoritmo principal: {end - start:.2f} segundos')

for juz in juzgados:
	print(f'Juzgado N {juz.numero}. Causas asignadas: {juz.causas_asignadas}. Gravedad acumulada: {juz.gravedad_acumulada}')
print(f'Total causas asignadas: {sum(juz.causas_asignadas for juz in juzgados)}')
#df = df.assign(juzgado_asignado=juzgados_asignados)
#df.to_excel('juzgados_asignados.xls')
#u = df['exp_cuerpos'].unique()
#print(u)

# Data to plot
labels = [juz.numero for juz in juzgados]
sizes = [juz.causas_asignadas for juz in juzgados]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
#explode = (0.1, 0, 0, 0)  # explode 1st slice
# Plot
plt.pie(sizes, labels=labels)
plt.axis('equal')
plt.show()
