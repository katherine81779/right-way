import json
import urllib.parse
import urllib.request

BASE_URL = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&' # this is to get the model id

def getModelID():
    brand = input()
    year = input()
    model = input()

    query_parameters = [('make', brand), ('model', model), ('year', year)]
    return BASE_URL + urllib.parse.urlencode(query_parameters)
    
def get_result(url):
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close
def printDescription(searchInfo):
    print(searchInfo['model_id'])

printDescription(get_result(getModelID()))
