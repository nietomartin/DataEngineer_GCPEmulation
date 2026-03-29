import pandas as pd
import numpy as np
import os

def generar_datos(n_rows, file_name):
    df = pd.DataFrame({
        "id_transaccion": np.arange(n_rows),
        "fecha": pd.date_range(start="2023-01-01", periods=n_rows, freq="s"),
        "cliente_id": np.random.randint(1, 100000, n_rows),
        "producto_id": np.random.randint(1, 1000, n_rows),
        "categoria": np.random.choice(["medicamentos", "equipos", "servicios"], n_rows),
        "cantidad": np.random.randint(1, 10, n_rows),
        "precio_unitario": np.random.uniform(10, 500, n_rows),
        "ciudad": np.random.choice(["Bogotá", "Cali", "Medellín","Popayán","Pasto","Pereira","Manizales","Barranquilla","Neiva","Tunja","Cartagena","Santa Marta"], n_rows),
        "canal": np.random.choice(["web", "app", "presencial"], n_rows),
        "estado": np.random.choice(["completado", "cancelado"], n_rows)
    })

    df.to_csv(file_name, index=False)

os.makedirs("data/raw", exist_ok=True)

for i in range(4):
    generar_datos(5_000_000, f"data/raw/ventas_part_{i+1}.csv")
