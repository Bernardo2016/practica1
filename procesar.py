import csv
import json

archivo_entrada = 'Estados.txt'
archivo_salida = 'resultado.txt'
resultados = []

try:
    with open(archivo_entrada, mode='r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # Filtro: Solo estados con Costo de Alojamiento menor a 1000
            if int(fila['Costo_Alojamiento']) < 1000:
                resultados.append(fila)

    with open(archivo_salida, mode='w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=4)
        
    print(f"Exito: resultado.txt generado con {len(resultados)} registros.")
except Exception as e:
    print(f"Error procesando datos: {e}")
