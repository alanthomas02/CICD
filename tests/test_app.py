#for testing app.p
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

def test_hello():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello world" in response.data 