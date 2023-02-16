import re
import os

bar = '''
---

School of Mathematical Sciences

Zhejiang University

Hangzhou, 310027, China
'''


# 删除文档的front-matter
def delFront(text1):
    front_matter = re.compile('---')
    if front_matter.search(text1, 0) is None:
        return text1
    else:
        start_num = front_matter.search(text1, 0).regs[0][0]
        end_num = front_matter.search(text1, 1).regs[0][1]
        if start_num == 0:
            return text1[end_num:]
        else:
            return text1


# 将文档中的块转换为语雀格式的块
def defConvert(matched):
    return ':::info\n' + matched.group(1) + '\n:::'


def thmConvert(matched):
    return ':::warning\n' + matched.group(1) + '\n:::'


def exConvert(matched):
    return ':::success\n' + matched.group(1) + '\n:::'


def remarkConvert(matched):
    return ':::danger\n' + matched.group(1) + '\n:::'


def blockConvert(text):
    re_def = re.compile(r'```ad-def\ntitle:(.*?)\n```', flags=re.DOTALL)
    re_thm = re.compile(r'```ad-thm\ntitle:(.*?)\n```', flags=re.DOTALL)
    re_ex = re.compile(r'```ad-ex\ntitle:(.*?)\n```', flags=re.DOTALL)
    re_remark = re.compile(r'```ad-remark\ntitle:(.*?)\n```', flags=re.DOTALL)
    if re_def.search(text, 0) is not None:
        text = re_def.sub(defConvert, text)
    if re_thm.search(text, 0) is not None:
        text = re_thm.sub(thmConvert, text)
    if re_ex.search(text, 0) is not None:
        text = re_ex.sub(exConvert, text)
    if re_remark.search(text, 0) is not None:
        text = re_remark.sub(remarkConvert, text)
    return text


# 删除文章中的Wiki链接
def wikiConvert(matched):
    return matched.group(1)


def delWiki(text1):
    re_wiki = re.compile('\[\[(.*?)]]')
    if re_wiki.search(text1, 0) is None:
        return text1
    else:
        text1 = re_wiki.sub(wikiConvert, text1)
        return text1


# def nnConvert(text):
#     re_nn = re.compile('\n\n')
#     text = re_nn.sub('\n', text)
#     return text


# 将各种处理程序合成为整个程序
def textConvert(text):
    text = delFront(text)
    text = blockConvert(text)
    text = delWiki(text)
    # text = nnConvert(text)
    return text


if __name__ == '__main__':
    os.chdir('docs')
    file_list = os.listdir()
    for item in file_list:
        file_input = open(item)
        data = file_input.read()
        file_input.close()
        data = textConvert(data)
        data += bar
        file_output = open(item, 'w')
        file_output.write(data)
        file_output.close()
