from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

print(client.list_buckets())

bucket_name = "bronze"

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

client.fput_object(bucket_name, "ventas_processed.csv", "data/processed/ventas_processed.csv")

print("Archivo subido a MinIO")