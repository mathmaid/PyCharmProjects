###################################################
# Userpath: 语雀个人路径最后的内容, 可以在账户设置中修改, 如路径为https://www.yuque.com/mathmaid, 则Userpath为mathmaid
# Repopath: 知识库的路径名, 可以在知识库设置中修改, 如路径为https://www.yuque.com/mathmaid/math, 则Repopath为math
# Docpath：文档的路径名, 可以在文档设置中修改, 如路径为https://www.yuque.com/mathmaid/math/curvature, 则Docpath为curvature
###################################################
import requests
import uuid
import os
import TextConverter
from constFile import base_url, user_path, headers_get, headers_post, escape_words
from YuqueData import getUserData, getReposData, getDocsData


# 输入Userpath, 返回Username
def userPathToName(Userpath):
    data = getUserData(Userpath)
    return data['name']


# 搜索路径Userpath中名为Reponame的知识库, 如果搜索成功返回Repopath, 否则输出没有知识库
def repoNameToPath(Userpath, Reponame):
    data = getReposData(Userpath)
    user_name = userPathToName(Userpath)
    for item2 in data:
        if item2['name'] == Reponame:
            return item2['slug']
    print('用户「' + user_name + "」没有名为「" + Reponame + "」的知识库")


# 搜索路径Userpath中在知识库Reponame中名为Docname的文档, 如果搜索成功返回Docpath, 否则输出没有文档
def docNameToPath(Userpath, Reponame, Docname):
    repo_path = repoNameToPath(Userpath, Reponame)
    user_name = userPathToName(Userpath)
    data = getDocsData(Userpath, repo_path)
    for item1 in data:
        if item1['title'] == Docname:
            return item1['slug']
    print('用户「'+user_name+'」的知识库「'+Reponame+"」下没有名为「"+Docname+"」的文档")


# 将Docname文件发布到Reponame知识库下, 此处需要注意, 语雀为了防止修改文档路径导致的误处理, 操作文档API时需要使用文档数据的唯一标识符ID.
# 实现思路为在Reponame知识库下检索有无Docname文件, 有则删除, 无则上传.
# Repopath和Docpath均由uuid自动生成
def postDoc(Userpath, Reponame, Docname):
    repo_path = repoNameToPath(Userpath, Reponame)
    data = getDocsData(Userpath, repo_path)
    for item3 in data:
        if item3['title'] == Docname:
            doc_id = item3['id']
            response = requests.delete(base_url+'repos/'+Userpath+'/'+repo_path+'/docs/'+str(doc_id),
                                       headers=headers_get)
            print("文档「"+Docname+"」已在知识库「"+Reponame+"」中删除，请求状态码为"+str(response.status_code))
    text = open(Docname + '.md').read()
    text = TextConverter.textConvert(text)

    data_upload = {
        'title': Docname,
        'slug': uuid.uuid1().hex,
        'body': text
    }
    response = requests.post('https://www.yuque.com/api/v2/repos/'+Userpath+'/' + repo_path + '/docs',
                             json=data_upload, headers=headers_post)
    print('在知识库「'+Reponame+"」中创建名为「"+Docname+"」的文档，请求状态码为"+str(response.status_code))


# 创建知识库
def postRepo(Username, Reponame):
    data = getReposData(Username)
    for item4 in data:
        if item4['name'] == Reponame:
            print('知识库「'+Reponame+"」已经存在")
            return True
    data_upload = {
        'name': Reponame,
        'type': 'Book',
        'slug': uuid.uuid4().hex,
        'public': 1
    }
    response = requests.post('https://www.yuque.com/api/v2/users/mathmaid/repos',
                             json=data_upload, headers=headers_post)
    print("已成功创建知识库「"+Reponame+"」，请求状态码为"+str(response.status_code))


# 获取当前文件夹下的所有文件夹(名称中不包含.的文件)
def getDirNames():
    listdir = os.listdir()
    pop_num = []
    for i in range(len(listdir), 0, -1):
        if '.' in listdir[i - 1]:
            pop_num.append(i - 1)
    for item5 in pop_num:
        listdir.pop(item5)
    return listdir


if __name__ == '__main__':
    dir_list = getDirNames()
    for item in dir_list:
        if item not in escape_words:
            postRepo(user_path, item)
            os.chdir(item)
            file_list = os.listdir()
            for doc in file_list:
                if doc not in escape_words:
                    postDoc(user_path, item, doc[0:-3])
            os.chdir('../')
