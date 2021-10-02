#This API is about Covid 19 cases, deaths and recovery per country
import requests
jsonResponse = requests.get("https://covid-api.mmediagroup.fr/v1/cases")
print(jsonResponse.status_code)
