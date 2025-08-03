from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

@app.route("/facturas")
def obtener_facturas():
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)
    df = pd.read_sql("SELECT * FROM facturas", engine)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
