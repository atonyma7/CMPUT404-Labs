import requests
print (requests.__version__)
requests.get('http://www.google.com')
my_request = requests.get('https://raw.githubusercontent.com/atonyma7/CMPUT404-Labs/main/lab_1.py')
print(my_request.text);