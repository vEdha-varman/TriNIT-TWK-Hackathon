from time import sleep
# import urllib
# import http
import requests

a = 0
b = 1
c = 0
# baseURL = 'http://api.thingspeak.com/update?api_key=2VMXN8ACSXG7M4YN&field1='
while(a < 400):
    print(a)
    
    r = requests.get(url=f"http://api.thingspeak.com/update?api_key=2VMXN8ACSXG7M4YN&field1={var1}&field2={var2}")
    
    print(r)

    sleep(5)
    c = a
    a = a + b
    b = c
print("Program has ended")
