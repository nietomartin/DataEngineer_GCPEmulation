# Data Engineering GCP Lab (Simulación local)

Este repositorio constituye un ejercicio de preparación para un cargo de Data Engineer para una entidad del sector salud, la cual utiliza fundamentalmente herramientas del ecosistema Google (GCP).

El ejercicio utiliza herramientas emuladoras de este sistema presentando un pipeline con cuatro archivos de 250 Mg para un total de una carga de 1Gb, utilizando una arquitectura Medallion y finalmente presentando una API con un microservicio con un reporte Json.

## 🚀 Arquitectura

CSV (1GB)
→ Ingesta (Python chunks)
→ Data Lake (MinIO)
→ Transformación (Pandas / Beam)
→ Serving (Flask API)

## 🧠 Tecnologías

- Python
- Apache Beam
- MinIO (GCS simulado)
- Docker
- PostgreSQL
- Flask

## ▶️ Scripts desarrollados

Una vez levantado el ambiente local (docker-compose up -d), la simulación del proceso se basa en los scripts:

1. **Generación de datos :**  src/ingestion/generate_data.py

2. **Procesamiento de chunks :**  src/ingestion/ingest_chunks.py

3. **Carga al Data Lake :**  src/storage/upload_minio.py

4. **Transormación de datos :**  src/processing/transform_pandas.py

## 🌐 API

http://localhost:5000/ventas

<table>
  <tr>
    <th>Preparado por</th>
    <th></th>
  </tr>
  <tr>
    <td><img src="img/martin.png" width="150"></td>
    <td>
      <strong>Ing. Martin Alfonso Nieto Prada</strong><br>
      mail: martinieto@gmail.com<br>
      <a href="https://github.com/nietomartin">https://github.com/nietomartin</a>
    </td>
  </tr>
</table>