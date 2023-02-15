import requests
import sqlalchemy
import pandas
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker, declarative_base
from constFile import my_license, user_name, password, database_name
import json

# 连接本地mysql中名为stock的数据库

# con_insert用于插入和改变数据, con_select用于查询数据
con_insert = sqlalchemy.create_engine('mysql+pymysql://'+user_name+':'+password
                                      + '@localhost:3306/'+database_name+'?charset=utf8')
con_select = con_insert.connect()
# session用于删除操作
Base = declarative_base()
DBsession = sessionmaker(bind=con_insert)
session = DBsession()


# 声明类，信息与数据库保持一致
class StockInfo(Base):
    __tablename__ = 'stock_info'
    dm = Column(String(10), primary_key=True)
    mc = Column(String(10))
    jys = Column(String(10))


class NewStockInfo(Base):
    __tablename__ = 'newstock_info'
    zqdm = Column(String, primary_key=True)
    zqjc = Column(String)
    sgdm = Column(String)
    fxsl = Column(Integer)
    swfxsl = Column(Integer)
    sgsx = Column(Integer)
    dgsz = Column(Integer)
    sgrq = Column(String)
    fxjg = Column(Float)
    zxj = Column(Float)
    srspj = Column(Float)
    zqgbrq = Column(String)
    zqjkrq = Column(String)
    ssrq = Column(String)
    syl = Column(Float)
    hysyl = Column(Float)
    wszql = Column(Float)
    yzbsl = Column(Float)
    zf = Column(Float)
    yqhl = Column(Float)
    zyyw = Column(String)


class StockFundFlow(Base):
    __tablename__ = 'stock_fund_flow'
    dm = Column(String, primary_key=True)
    t = Column(String, primary_key=True)
    zdf = Column(Float)
    lrzj = Column(Float)
    lrl = Column(Float)
    lczj = Column(Float)
    jlr = Column(Float)
    jlrl = Column(Float)
    shlrl = Column(Float)


class HistoryDeal(Base):
    __tablename__ = 'history_deal'
    dm = Column(String, primary_key=True)
    t = Column(String, primary_key=True)
    c = Column(Float)
    zdf = Column(Float)
    jlrl = Column(Float)
    hsl = Column(Float)
    qbjlr = Column(Float)
    cddlr = Column(Float)
    cddjlr = Column(Float)
    ddlr = Column(Float)
    ddjlr = Column(Float)
    xdlr = Column(Float)
    xdjlr = Column(Float)
    sdlr = Column(Float)
    sdjlr = Column(Float)


# 更新沪深两市股票信息
def updateStock():
    url = 'http://api.mairui.club/hslt/list/' + my_license
    response = requests.get(url)
    list_stock = json.loads(response.text)
    df1 = pandas.DataFrame(list_stock)
    df1.columns = ['dm', 'mc', 'jys']
    for i in range(len(df1['jys'])):
        if df1['jys'][i] == 'sz':
            df1.loc[i, 'jys'] = '深证'
        if df1['jys'][i] == 'sh':
            df1.loc[i, 'jys'] = '上证'
    session.query(StockInfo).delete()
    session.commit()
    session.close()
    df1.to_sql('stock_info', con=con_insert, if_exists='append', index=False)
    print('操作成功')


# 更新沪深两市新股日历
def updateNewStock():
    url = 'http://api.mairui.club/hslt/new/' + my_license
    response = requests.get(url)
    list_stock = json.loads(response.text)
    df1 = pandas.DataFrame(list_stock)
    session.query(NewStockInfo).delete()
    session.commit()
    session.close()
    df1.to_sql('newstock_info', con=con_insert, if_exists='append', index=False)
    print('操作成功')


# 更新股票主力资金走向
def updateStockFundFlow(stock_id):
    url = 'http://api.mairui.club/hsmy/zlzj/' + stock_id + '/' + my_license
    response = requests.get(url)
    data_json = json.loads(response.text)
    df3 = pandas.DataFrame(data_json)
    df3['dm'] = stock_id
    # session.query(StockFundFlow).delete()
    # session.commit()
    # session.close()
    df3.to_sql('stock_fund_flow', con=con_insert, if_exists='append', index=False)
    print('操作成功')


# 更新股票历史十年成交数据
def updateStockHistoryDeal(stock_id):
    url = 'http://api.mairui.club/hsmy/lscj/' + stock_id + '/' + my_license
    response = requests.get(url)
    data_json = json.loads(response.text)
    try:
        df3 = pandas.DataFrame(data_json)
        df3['dm'] = stock_id
    # session.query(HistoryDeal).delete()
    # session.commit()
    # session.close()
        df3.to_sql('history_deal', con=con_insert, if_exists='append', index=False)
        print('操作成功')
        return True
    except:
        print('操作失败')
        return False


def getStockInfo():
    sql = 'SELECT * from stock_info where dm >= 56'
    sql_query = text(sql)
    df = pandas.read_sql(sql_query, con=con_select)
    return df


if __name__ == '__main__':
    updateStock()
    updateNewStock()
    updateStockFundFlow('000001')
    updateStockHistoryDeal('000001')
