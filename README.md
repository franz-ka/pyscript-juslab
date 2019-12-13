# pyscript-juslab
#JusLab - Script para asignar causas judiciales por sorteo a los distintos juzgados

El script [export_delitos_unique.py](export_delitos_unique.py) exporta los tipos de delitos únicos
del csv [penal_df.csv](penal_df.csv) (mirando el campo id de los delitos *oju_id*).

El script [main.py](main.py) lee ese archivo (renombrado a
*Tipos de delitos por complejidad - tipos-delitos.csv*)
y reparte secuencialmente por sorteo todas las causas de la planilla [penal_df.csv](penal_df.csv)
a los 31 distintos juzgados, teniendo en consideración repartir equitativamente las causas según
las gravedades de las mismas. De esta forma balancea la carga de trabajo entre todos los juzgados equitativamente.
