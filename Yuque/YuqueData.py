###################################################
# 模块YuqueData提供五个函数, 分别用以获取不同的语雀数据流
# Userpath: 语雀个人路径最后的内容, 可以在账户设置中修改, 如路径为https://www.yuque.com/mathmaid, 则Userpath为mathmaid
# Repopath: 知识库的路径名, 可以在知识库设置中修改, 如路径为https://www.yuque.com/mathmaid/math, 则Repopath为math
# Docpath：文档的路径名, 可以在文档设置中修改, 如路径为https://www.yuque.com/mathmaid/math/curvature, 则Docpath为curvature
# getUserData(Userpath): 返回值为用户信息, 数据类型为dict
# getReposData(Userpath): 返回值为某一用户的所有知识库的基本信息, 数据类型为list, 其中的元素为dict
# getRepoData(Userpath, Repopath): 返回某一用户的某一知识库的详细信息, 数据类型为dict
# getDocsData(Userpath, Repopath): 返回某一用户的某一知识库下的文档的基本信息, 数据类型为list, 其中的元素为dict
# getDocData(Userpath, Repopath, Docpath): 返回某一用户的某一知识库下的某一文档的详细信息, 数据类型为dict
###################################################
import requests
import json
from constFile import base_url, headers_get


def getUserData(Userpath):
    response = requests.get(base_url + "users/" + Userpath, headers=headers_get)
    data = response.text
    data_json = json.loads(data)
    return data_json["data"]


def getReposData(Userpath):
    response = requests.get(base_url+"users/"+Userpath+"/repos", headers=headers_get)
    data = response.text
    data_json = json.loads(data)
    return data_json["data"]


def getRepoData(Userpath, Repopath):
    response = requests.get(base_url + "repos/" + Userpath + "/" + Repopath, headers=headers_get)
    data = response.text
    data_json = json.loads(data)
    return data_json["data"]


def getDocsData(Userpath, Repopath):
    response = requests.get(base_url + "repos/" + Userpath + "/" + Repopath + "/docs", headers=headers_get)
    data = response.text
    data_json = json.loads(data)
    return data_json["data"]


def getDocData(Userpath, Repopath, Docpath):
    response = requests.get(base_url + "repos/" + Userpath + "/" + Repopath + "/docs/" + Docpath, headers=headers_get)
    data = response.text
    data_json = json.loads(data)
    return data_json["data"]
