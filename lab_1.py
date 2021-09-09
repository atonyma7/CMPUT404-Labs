import requests
print (requests.__version__)
requests.get('http://www.google.com')
print(requests.get('https://github.com/atonyma7/CMPUT404-Labs/blob/main/lab_1.py').request.body);