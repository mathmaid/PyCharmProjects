import time
import pandas
import bs4
import re
from selenium import webdriver

# 提出出来的Product Code和title自带前缀，用正则表达式处理
find_code = re.compile('Product Code: (.*)')
find_title = re.compile('\n(.*)')

# 定义用于存储信息的变量
data = []

# 设置系列书籍基础url，在其后添加page属性
base_url = 'https://bookstore.ams.org/gsm'

# 用webdriver定义浏览器对象并将浏览器最大化
browser = webdriver.Safari()
browser.maximize_window()

for num in range(0, 5):
    browser.get(base_url+'?page='+str(num))
    # 此处的sleep用于等待页面完全加载完毕，生成完整的html
    time.sleep(10)
    # 获取网页的html源码
    html = browser.page_source
    soup = bs4.BeautifulSoup(html, 'lxml')

    Title_list = soup.select('h4')
    Product_list = soup.select('.baseProductCode')
    Author_list = soup.select('.browseAuthors')
    for i in range(len(Title_list)):
        data.append({
            'product_code': find_code.findall(Product_list[i].text)[0],
            'title': Title_list[i].text,
            'series': find_title.findall(soup.h1.text)[0],
            'author': Author_list[i].text,
            'type': '',
            'tags': ''
        })

# 关闭浏览器
browser.close()
table_books = pandas.DataFrame(data).set_index('product_code')
table_books.to_csv('booklist.csv')

# selenium还可以利用语句找出特定的元素
# input = browser.find_element(by=By.CSS_SELECTOR, value='h1')
# 找到元素后可以使用click(), send_keys()等方法进行交互操作
# 需要注意的是在寻找元素时所引用的By需要提前声明
# from selenium.webdriver.common.by import By
