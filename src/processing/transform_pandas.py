import pandas as pd

df = pd.read_csv("data/processed/ventas_processed.csv")

df_filtered = df[df["estado"] == "completado"]

result = df_filtered.groupby(["ciudad", "categoria"])["total"].sum().reset_index()

result.to_csv("data/curated/ventas_aggregadas.csv", index=False)

print("Transformación completada")

