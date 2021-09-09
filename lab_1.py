import requests
print (requests.__version__)
requests.get('http://www.google.com')
print(requests.get('https://raw.githubusercontent.com/atonyma7/CMPUT404-Labs/main/lab_1.py').request.body);