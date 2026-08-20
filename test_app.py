import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Añadir la carpeta backend al path para importar app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Importar la app Flask
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch('app.pymysql.connect')
    def test_status_ok(self, mock_connect):
        # Simular conexión exitosa a la base de datos
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_connect.return_value = mock_conn

        response = self.client.get('/api/status')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('Mensaje equivocado', data['message'])  # Esto fallará
