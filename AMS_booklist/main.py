import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
}

url = 'https://bookstore.ams.org/product/browseproducts'

data = {
    # MIME类型: application/x-www-form-urlencoded; charset=UTF-8
    'filterString': 'Series=GSM',
    'pageNumber': 1,
    'numPerPage': 230,
    'sortBy': 'DATE_DESC'
}

response = requests.post(url, data=data, headers=headers)

