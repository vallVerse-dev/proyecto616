from flask import Flask, jsonify
from flask_cors import CORS
import pymysql
import os

MYSQL_PASSWORD = "Clave_123"

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'testdb'),
        user=os.environ.get('DB_USER', 'user'),
        password=os.environ.get('DB_PASSWORD', 'password'),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/api/status')
def status():
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute('SELECT 1')
        conn.close()
        return jsonify({"message": "Error simulado"}), 500
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('HOST', '127.0.0.1'), port=5050, debug=True)
