import boto3

def validar():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Cambia tu región si es necesario
    tabla = dynamodb.Table('TablaEstados')
    
    print("--- INICIANDO LECTURA DE DYNAMODB ---")
    respuesta = tabla.scan()
    items = respuesta.get('Items', [])
    
    for item in items:
        estado = item.get('Estado')
        # Ejemplo de validación: Verificar que el costo de alojamiento sea mayor a 0
        costo_alojamiento = int(item.get('Costo_Alojamiento', 0))
        
        if costo_alojamiento > 0:
            print(f"[SUCCESS] El estado {estado} tiene un costo de alojamiento válido: ${costo_alojamiento}")
        else:
            print(f"[ERROR] El estado {estado} tiene un costo de alojamiento inválido.")

if __name__ == "__main__":
    validar()
