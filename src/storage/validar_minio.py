from minio import Minio
import pandas as pd
import io

# conexión
client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

bucket_name = "bronze"
file_name = "ventas_processed.csv"

# 1. validar bucket
if not client.bucket_exists(bucket_name):
    print("❌ Bucket no existe")
    exit()

print("✅ Bucket existe")

# 2. listar archivos
objects = list(client.list_objects(bucket_name))
print(f"📂 Archivos en bucket: {[obj.object_name for obj in objects]}")

# 3. validar archivo
obj = client.get_object(bucket_name, file_name)

# leer primeras líneas
data = obj.read(1024 * 10)  # primeros KB
print("📄 Preview archivo:")
print(data.decode("utf-8")[:500])

# 4. contar filas (aproximado)
obj = client.get_object(bucket_name, file_name)
df = pd.read_csv(io.BytesIO(obj.read()), nrows=10000)

print(f"🔢 Filas leídas (sample): {len(df)}")

print("✅ VALIDACIÓN COMPLETA")