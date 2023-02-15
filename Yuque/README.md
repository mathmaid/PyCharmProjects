# Yuque

语雀提供了用API查询语雀知识库数据和文档数据的解决方案

在使用本程序前需要在Yuque目录下提供一个名为constFile.py的文件, 其内容如下:

```python
user_path = '语雀用户路径, 可以在设置中查找'
token = '语雀用户Token，可以在设置中生成'


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
```
## YuqueData

YuqueData是本程序的核心模块，提供五个函数, 分别用以获取不同的语雀数据

1. getUserData(Userpath): 返回值为用户信息, 数据类型为dict
2. getReposData(Userpath): 返回值为某一用户的所有知识库的基本信息, 数据类型为list, 其中的元素为dict
3. getRepoData(Userpath, Repopath): 返回某一用户的某一知识库的详细信息, 数据类型为dict
4. getDocsData(Userpath, Repopath): 返回某一用户的某一知识库下的文档的基本信息, 数据类型为list, 其中的元素为dict
5. getDocData(Userpath, Repopath, Docpath): 返回某一用户的某一知识库下的某一文档的详细信息, 数据类型为dict

其中输入的变量分别为

1. Userpath: 语雀个人路径最后的内容, 可以在账户设置中修改, 如路径为https://www.yuque.com/mathmaid, 则Userpath为mathmaid
2. Repopath: 知识库的路径名, 可以在知识库设置中修改, 如路径为https://www.yuque.com/mathmaid/math, 则Repopath为math
3. Docpath：文档的路径名, 可以在文档设置中修改, 如路径为https://www.yuque.com/mathmaid/math/curvature, 则Docpath为curvature

