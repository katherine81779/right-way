import json
import urllib.parse
from urllib.request import Request, urlopen
import requests

BASE_URL = 'https://www.carqueryapi.com/api/0.3/?cmd=getTrims&' # this is to get the model id

def getBasicURL(brand, model, year):
    query_parameters = [('make', brand), ('model', model), ('year', year)]
    theStatement = BASE_URL + urllib.parse.urlencode(query_parameters)
    return theStatement
    
def getBasicResult(url):
    response = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    json_text = urlopen(response).read()
    return json.loads(json_text)

def getCarDictBase(searchInfo):
    carDict = searchInfo['Trims'][0]
    return carDict