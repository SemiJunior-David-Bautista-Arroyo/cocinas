import os
import json
from jwt import encode, decode

credenciales = '../credenciales.json'

with open(credenciales, 'r') as c:
    clave = json.load(c)


def create_token(data : dict):
    token : str = encode(payload=data, key=clave, algorithm='HS256')

    return token


def validate_token(token : str) -> dict:

    data : dict = decode(token, key= clave)






