import pandas
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
}

url = 'https://bookstore.ams.org/product/browseproducts'

data = {
    # MIME类型: application/x-www-form-urlencoded; charset=UTF-8
    'filterString': 'Series=GSM',
    'pageNumber': 1,
    # 总书籍数量，需要随时更新
    'numPerPage': 230,
    'sortBy': 'DATE_DESC'
}

response = requests.post(url, data=data, headers=headers)

# 进行数据清洗

data = json.loads(response.text)
data = data['Products']
df = pandas.DataFrame(data)
df1 = df[['CopyrightYear','ProductCode','RelatedCustomers','Title','Subtitle','ProductDescription']]

# TODO 将信息中的作者信息和机构信息提取出来
df1.columns = ['出版年','序列号','信息','标题','副标题','简介']


df1.to_csv('booklist.csv')