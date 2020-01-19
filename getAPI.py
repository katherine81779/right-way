import json
import urllib.parse
from urllib.request import Request, urlopen
import requests

BASE_URL = 'https://www.carqueryapi.com/api/0.3/?cmd=getTrims&' # this is to get the model id

def getBasicURL(brand, model, year):
    query_parameters = [('make', brand), ('model', model), ('year', year)]
    return BASE_URL + urllib.parse.urlencode(query_parameters)
    
def getBasicResult(url):
    response = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    json_text = urlopen(response).read()
    return json.loads(json_text)

def getCarDictBase(searchInfo):
    carDict = searchInfo['Trims'][0]
    return carDict

# BASEURL is formed in app.py file
baseURL = "" 
modelInfo = getCarDictBase(getBasicResult(baseURL))

modelID = modelInfo['model_id']

# Things that we need to print
bodyType = modelInfo['model_body']
seatsNum = modelInfo['model_seats']
doorsNum = modelInfo['model_doors']
origin = modelInfo['make_country']
weight = modelInfo["model_weight_kg"] # Display: heavier cars makes it safer to drive
length = modelInfo["model_length_mm"] 
width = modelInfo["model_width_mm"]
height = modelInfo["model_height_mm"] # Display: Taller people should get taller cars for comfortable driving

family = "Not Friendly"
if (int(seatsNum) >= 4 and int(doorsNum) >=4):
    family = "Friendly"

info = [modelID, bodyType, seatsNum, doorsNum, origin, weight, length, width, height]

for i in range(len(info)):
    if (info[i] == None):
        info[i] = "Not Available"
