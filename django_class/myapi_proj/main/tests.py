# from django.test import TestCase

# # Create your tests here.
import requests


url = "http://127.0.0.1:8000/v1/users/"

res = requests.get(url, headers={
    'Authorization' : 'Token 1ed4c242f7e58f15dd2c32e69c89a04cb805858b'})
print(res.status_code)
print(res.json())
