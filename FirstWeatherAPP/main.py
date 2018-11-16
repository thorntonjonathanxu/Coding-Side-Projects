import requests,json

# zip = '45207'
# country = 'us'
# base_api = "https://api.openweathermap.org/data/2.5/weather?zip={0},{1}".format(zip,country)
# # print(base_api)
# user_api = '74998832e35cc183342c847c5d93dd53'
# unit = 'metric'
# full_api_url = base_api + '&mode=json&units=' + unit + '&APPID=' + user_api
# print(full_api_url)
# r = requests.get(full_api_url)
# data = r.json()
# with open('Export_test.json','w+') as f:
#     json.dump(data,f)
# print('Finished Exporting JSON')

with open('Export_test.json','r') as f:
    parsed = json.load(f)
    print(parsed)