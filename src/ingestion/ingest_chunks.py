import pandas as pd
import glob

files = glob.glob("data/raw/*.csv")
chunk_size = 500000

output_file = "data/processed/ventas_processed.csv"

for file in files:
    print(f"Procesando {file}")

    for chunk in pd.read_csv(file, chunksize=chunk_size):
        chunk["total"] = chunk["cantidad"] * chunk["precio_unitario"]

        chunk.to_csv(output_file, mode="a", header=not pd.io.common.file_exists(output_file), index=False)