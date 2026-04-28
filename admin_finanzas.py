import boto3
from datetime import datetime

def administrar_reporte():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    s3 = boto3.client('s3')
    tabla = dynamodb.Table('MusicaSpotify')
    
    # Simular una modificación de "venta/ajuste" (Requisito de la empresa)
    cancion_target = "Blinding Lights"
    ahora = datetime.now()
    
    tabla.update_item(
        Key={'Cancion': cancion_target},
        UpdateExpression="set FechaModificacion = :f, HoraModificacion = :h, Editor = :e",
        ExpressionAttributeValues={
            ':f': ahora.strftime("%Y-%m-%d"),
            ':h': ahora.strftime("%H:%M:%S"),
            ':e': 'Ingeniero_Sanchez_Gomez'
        }
    )

    # Generar el archivo .txt para Finanzas México
    items = tabla.scan()['Items']
    ruta_local = '/tmp/reporte_finanzas.txt'
    
    with open(ruta_local, 'w') as f:
        f.write("REPORTE FINANCIERO - DEPARTAMENTO MEXICO\n")
        f.write(f"Corte al: {ahora.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n")
        for i in items:
            f.write(f"ELEMENTO: {i['Cancion']} | ULTIMA EDICION: {i.get('FechaModificacion', 'ORIGINAL')} | POR: {i.get('Editor', 'SISTEMA')}\n")

    # Subir al bucket para que Finanzas lo tenga listo
    s3.upload_file(ruta_local, 'act.20.04', 'reporte_finanzas_mexico.txt')
    print("Reporte generado exitosamente en S3.")

if __name__ == "__main__":
    administrar_reporte()
