#importando as bibliotecas
import json
import folium
import requests
import csv
import os  

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados?formato=application/vnd.geo+json"
json_dados= requests.get(url).json()
nomes = [x['nome'] for x in json_dados if x['nome'].startswith("A") ]
# print("nomes que começam com A: ",nomes)

nomes = [x['nome'] for x in json_dados if x['nome'].endswith("o") ]
# print("nome que termina com o",nomes)

nomes = [x['regiao']['nome'] for x in json_dados]
# print("Regiões: ",nomes)



import pandas as pd

location = "https://data.smartdublin.ie/dataset/33ec9fe2-4957-4e9a-ab55-c5e917c7a9ab/resource/2dec86ed-76ed-47a3-ae28-646db5c5b965/download/dublin.csv"
bike_station_locations_file = requests.get(location).content.decode('utf-8').split("\n")

bike_station_locations=[x.split(",") for x in bike_station_locations_file]
# print(bike_station_locations)

url = "https://raw.githubusercontent.com/datalivre/Conjunto-de-Dados/master/br_states.json?formato=application/vnd.geo+json"

geo_json_data= requests.get(url).json()


