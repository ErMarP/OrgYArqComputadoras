# Biblioteca para leer el nombre del archivo
import sys
# Biblioteca para verificar si un archivo existe
import os.path

contador = 0

bandera = ''
archivo = ''

if(len(sys.argv) >0):
    for i in range(1, 3):
        if(sys.argv[i] == '-f' or sys.argv[i] == '-d'):
            bandera = sys.argv[i]
        else:
            archivo = sys.argv[i]
# Verificamossi existe el archivo con los datos
if(not os.path.isfile(archivo)):
    print("No se encontró el archivo")
    sys.exit()

# Leemos el archivo
arch = open(archivo)
indice = 0
# Iterar sobre las líneas del archivo
suma_tiempos = 0
for x in arch:
    datos = x.split()
    if(indice == 0):
        operaciones_procesador = x
    elif(len(datos) == 2):
        # Realizamos el cálculo directo con la instruccion iésima, los ciclos de ejcución y  el número de apariciones que tiene
        suma_tiempos = suma_tiempos + int(datos[0]) * int(datos[1])
    indice = indice + 1

# Regresar el resultado
if(bandera == '-d'):
    print("Tiempo total: "+str(suma_tiempos * float(datos[0])))
else:
    print("Tiempo total: "+str(suma_tiempos * (1/float(datos[0]))))

''' Ecuación del desempeño
Tiempo del programa = (instrucciones del programa X ciclos de reloj)/frecuencia
                                    d = 1 / f
t1 + t2 + t3 + ... + tn
en donde ti = (i.p X ciclos)/f

(i.p X ciclos)/f (i.p X ciclos)/f  (i.p X ciclos)/f  (i.p X ciclos)/f

factorizamos

(1/f) [ (i.p X ciclos) + (i.p X ciclos) + (i.p X ciclos) + (i.p X ciclos) ]

'''
