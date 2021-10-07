#This API is about Covid 19 cases, deaths and recovery per country
import requests
Response = requests.get("https://covid-api.mmediagroup.fr/v1/cases")
print(Response.status_code)
Response.json()