# Stock

Stock利用麦蕊智数的API爬取沪深两市股票基本信息、沪深两市新股日历，主力资金走势、历史成交分布(十年)等数据

使用此程序前需要在同级目录下创建一个constFile.py文件，并且在其中输入

```python
my_license = '从麦蕊智数获取的license文本'
user_name = '数据库管理员用户名'
password = '数据库管理员密码'
database_name = '存储股票数据信息的数据库名称'
```

需要在数据库中创建表stock_info, newstock_info, stock_fund_flow, history_deal四个表, 具体的字段和创建表的代码可以在DataGripProjects中的Stock文件夹中找到

getStock.py中一共提供了四种方法：

1. 更新股票数据：updateStock()
2. 更新新股日历：updateNewStock()
3. 更新某一股票的资金走向：updateStockFundFlow(stock_id)
4. 更新某一股票的历史交易：updateStockHistoryDeal(stock_id)

main.py是获取所有股票十年历史交易数据的代码