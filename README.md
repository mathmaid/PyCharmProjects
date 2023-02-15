# PyCharmProjects项目

PyCharmProjects是一个数据收集项目，其中包含了从许多源中爬取的数据。

## AMS_booklist

美国数学协会(AMS)将指定的研究生数学教材公布在其官网上(需要科学上网)

[https://bookstore.ams.org/gsm](https://bookstore.ams.org/gsm)

但是数学书的数据通过动态加密的方式传输到本地

这个程序使用selenium模拟浏览器载入网页，通过获取网页源码来爬取教材数据，返回字段为product_code(书籍序列号), title(书籍标题), series(书籍系列), author(作者), type(类型), tags(标签), 爬取得到的数据将会储存在booklist.csv文件中

需要注意的是程序默认使用Safari浏览器，如果使用其他浏览器需要在webdriver中进行修改

程序依赖包：
1. pandas
2. bs4
3. re
4. selenium
5. time
6. lxml

