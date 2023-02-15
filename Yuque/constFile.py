user_path = 'mathmaid'
token = 'G6lNeslVypaHRrTyajEDp0VktH5vux2ciGm5DoVe'


base_url = "https://www.yuque.com/api/v2/"
headers_get = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'X-Auth-Token': token,
}

headers_post = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'X-Auth-Token': token,
    'Content-Type': 'application/json'
}

escape_words = ['.DS_Store', '__pycache__', '.idea']
