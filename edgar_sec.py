import requests
import json

def secDataPull():
    print('Calling Server')
    ##Builds and call a request using username and API Generated Key
    hyperlink = 'https://www.sec.gov/Archives/edgar/data/1122304/0001193125-15-118890.json'
    print('Intializing JSON Download')
    r = requests.get(hyperlink)
    data = r.json()
    print('Authorized connection. Loading names...')

    # Dumps all field values into a JSON file for temporary testing
    with open("ptest.json", "w") as f:
        json.dump(data,f)
    print('JSON Export Complete')
    # input_file = open ('test.json', 'r')
    # names_list = json.load(input_file)

secDataPull()