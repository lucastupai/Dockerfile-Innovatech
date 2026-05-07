import os 
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = 'db'  

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos:  {e}")
        return None
@app.route('/data')
def index():
    conn = get_db_connection()
    if conn:
        status = "Conexión exitosa a la base de datos"
        conn.close()
    else:
        status = "Error al conectar a la base de datos"
    return jsonify({
        "proyecto": "InnovaTech API",
        "estado_db": status,
        "v": "1.0.2"
    })

if __name__ == '__main__':
    app.run(host='0.0.0', port=8000)