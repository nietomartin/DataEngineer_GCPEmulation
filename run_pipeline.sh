#!/bin/bash

echo "Generando datos..."
python src/ingestion/generate_data.py

echo "Procesando chunks..."
python src/ingestion/ingest_chunks.py

echo "Subiendo a Data Lake..."
python src/storage/upload_minio.py

echo "Transformando datos..."
python src/processing/transform_pandas.py

echo "Pipeline completado"
