from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/facturas")
def obtener_facturas():
    engine = create_engine("postgresql+psycopg2://jhonvilcaranatintaya:JVT954416045@localhost:5432/postgres")
    df = pd.read_sql("SELECT * FROM facturas", engine)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
