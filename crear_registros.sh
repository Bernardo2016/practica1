#!/bin/bash
# Cambia el nombre del bucket aquí
BUCKET_LOGS="s3://mi-pagina2"
LOG_FILE="/tmp/insercion_dynamo.log"
# ... resto del código igual ...

# Registrar la fecha y hora de inicio
echo "=====================================" > $LOG_FILE
echo "Iniciando creación de registros en DynamoDB: $(date)" >> $LOG_FILE

# Ejecutar el script de Python y guardar la salida en el log
python procesar.py >> $LOG_FILE 2>&1

# Registrar el fin de la ejecución
echo "Creación finalizada: $(date)" >> $LOG_FILE
echo "=====================================" >> $LOG_FILE

# Subir el log al bucket en AWS
aws s3 cp $LOG_FILE $BUCKET_LOGS/logs_insercion.log
