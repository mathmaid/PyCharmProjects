import pandas
import requests
import json
from constFile import my_license

df = pandas.read_csv('Result_62.csv', dtype={0: "string"})

list_stock = []
for item in df['股票代码']:
    list_stock.append(item)


value_tomorrow = []
value_today = []
value_yesterday = []
count = 1
for item in list_stock:
    print('正在处理' + str(count) + '/' + str(len(list_stock)) + '条目:' + item)
    try:
        url = 'http://api.mairui.club/hsmy/lscj/' + item + '/' + my_license
        response = requests.get(url)
        data_json = json.loads(response.text)
        data_tomorrow = data_json[0]['zdf']
        data_today = data_json[1]['zdf']
        data_yesterday = data_json[2]['zdf']
        value_tomorrow.append(float(data_tomorrow))
        value_today.append(float(data_today))
        value_yesterday.append(float(data_yesterday))
        print('操作成功')
        count += 1
    except TypeError:
        print('操作失败')
        count += 1
        continue
