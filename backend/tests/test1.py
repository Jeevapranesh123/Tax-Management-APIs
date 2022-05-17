from fastapi.testclient import TestClient
from app.db import get_db
from app.main import app
import string
import random
import json

client = TestClient(app)

def random_char(char_num):
    return "".join(random.choice(string.ascii_letters) for _ in range(char_num))

class TestAuth:

    global_email=random_char(7)+'@gmail.com'
    global_password=random_char(7)
    def test_register(self):
        email=random_char(7)+'@gmail.com'
        password=random_char(8)
        payload={'email':self.global_email, 'password':self.global_password}
        response = client.post('/auth/register', data=json.dumps(payload))
        data=response.json()
        assert response.status_code == 200
        assert data['email'] == self.global_email
    
    def test_register1(self):
        password=random_char(8)
        payload={'email':self.global_email, 'password':password}
        response = client.post('/auth/register', data=json.dumps(payload))

        assert response.status_code==400
    
    def test_login(self):

        payload={'email':self.global_email, 'password':self.global_password}
        response = client.post("/auth/login",data=json.dumps(payload))
        assert response.status_code == 200

    def test_login1(self):

        email=random_char(7)+'@gmail.com'
        password=random_char(8)
        payload={'email':self.global_email, 'password':password}
        response = client.post("/auth/login",data=json.dumps(payload))
        assert response.status_code == 403
        
        payload={'email':email, 'password':password}
        response = client.post("/auth/login",data=json.dumps(payload))
        assert response.status_code == 404