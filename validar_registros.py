import boto3
import csv

def insertar_datos():
    s3 = boto3.client('s3')
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Ajusta tu región
    tabla = dynamodb.Table('TablaEstados')
    
    # Leer archivo desde S3
    respuesta = s3.get_object(Bucket='act.20.04', Key='Estados.txt')
    lineas = respuesta['Body'].read().decode('utf-8').splitlines()
    lector_csv = csv.DictReader(lineas)
    
    # Insertar en DynamoDB
    for fila in lector_csv:
        tabla.put_item(Item={
            'Estado': fila['Estado'],
            'Temperatura': int(fila['Temperatura']),
            'Humedad': int(fila['Humedad']),
            'Costo_Alojamiento': int(fila['Costo_Alojamiento']),
            'Costo_Transporte': int(fila['Costo_Transporte']),
            'Dias_Promedio': int(fila['Dias_Promedio']),
            'Tiempo_Traslado': int(fila['Tiempo_Traslado'])
        })
        print(f"Registro creado exitosamente: {fila['Estado']}")

if __name__ == "__main__":
    insertar_datos()
