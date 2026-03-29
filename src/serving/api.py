from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/ventas")
def ventas():
    df = pd.read_csv("data/curated/ventas_aggregadas.csv")
    return df.to_json(orient="records")

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
