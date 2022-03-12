import requests
import json

def avgRotorSpeed(statusQuery, parentId):
    totalRotorSpeed = 0
    count = 0
    s = "https://jsonmock.hackerrank.com/api/iot_devices/search?" + statusQuery + "&page=1"
    response = requests.get(s) 
    json_data = json.loads(response.text)
    pages = int (json_data['total_pages'])
    for i in range (pages):
        s = "https://jsonmock.hackerrank.com/api/iot_devices/search?" + statusQuery + "&page=" + str(i)
        response = requests.get(s) 
        json_data = json.loads(response.text)['data']
        for j in range (len (json_data)):
            if 'parent' in json_data[j]:
                if json_data[j]['parent'] != None and 'id' in json_data[j]['parent']:
                    if json_data[j]['parent']['id'] == parentId:
                        totalRotorSpeed += json_data[j]['operatingParams']['rotorSpeed']
                        count += 1
    if count == 0:
        return 0
    else:
        print(totalRotorSpeed // count)
        return totalRotorSpeed // count    

avgRotorSpeed ('STOP', 7)
