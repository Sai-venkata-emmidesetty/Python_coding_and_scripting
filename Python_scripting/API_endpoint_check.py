import requests
endpoint=input("enter the endpoint to check")

status_code_check=requests.get(endpoint).status_code

print(status_code_check)

#input=https://www.google.com
#200-> endpoint is good, otherwise it's not working
