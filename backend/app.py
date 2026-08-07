from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'testdb'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'ClaveSegura123')
    )
    return conn

@app.route('/api/status')
def status():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return jsonify({"message": "Conexión exitosa a la base de datos"})
    except Exception as e:
        return jsonify({"message": f"Error de conexión: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
