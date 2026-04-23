#!/bin/bash

# Variables
BUCKET_LOGS="s3://act.20.04"
LOG_FILE="/tmp/insercion_dynamo.log"

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
