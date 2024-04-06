'''
登录
各种签到
'''

import json
import requests
import base64
import re
import time
from lxml import etree
import js2py

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    "Referer": "https://passport2.chaoxing.com",
    "Origin": "https://passport2.chaoxing.com",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}
img = "static/head1.jpg"
def getcpi(cookies,courseid,classid):
    url = "http://mooc2-ans.chaoxing.com/visit/courses/list?v=1647437464895&rss=1&start=0&size=500&catalogId=0&searchname="
    r = requests.get(url,cookies=cookies,headers=headers)
    string = "courseid={}&clazzid={}&cpi=([0-9]+)".format(courseid,classid)
    
    cpi = re.findall(string, r.text)[0]
    

    

    return cpi
    #yiliangersan11?
    #9d8d512452c7f8355f1eb416f3bed3ed

def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()
    return result

def login(account,password):
    global cookies
    context = js2py.EvalJs()
    context.execute(js_from_file('crypto.js'))
    context.execute(js_from_file('util.js'))
    EncryptedAccount = context.encryptByAES(account, "u2oh6Vu^HWe4_AES")
    EncryptedPassword = context.encryptByAES(password, "u2oh6Vu^HWe4_AES")
    #encode_str = base64.encodebytes(password.encode('utf8'))
    #password_b64 = encode_str.decode()
    #cxlogin.login("15290223661","9d8d512452c7f8355f1eb416f3bed3ed")
    url = "https://passport2.chaoxing.com/fanyalogin"
    data={ 
        'fid': '-1',
        'uname': EncryptedAccount,
        'password': EncryptedPassword,
        'refer': 'http%3A%2F%2Fi.chaoxing.com',
        't': 'true',
        'forbidotherlogin': '0',
        'validate': '',
        'doubleFactorLogin': '0',
        'independentId': '0'
    }
    #print(data)
    r = requests.post(url,headers=headers,data=data)
    #print(r.text)
    
    cookies = r.cookies.get_dict()
    return str(r.json()["status"]),cookies

status,cookies = login("15290223661","yiliangersan11?")



url='https://mobilelearn.chaoxing.com/pptSign/stuSignajax'
data = {
'name':'王书浩',
'address':'华北理工大学冀唐学院',
'activeId':"3000089919377",
'uid':'152373457',
'clientip':'',
'latitude':'39.213833', #39.213833
'longitude':'118.594513', #118.594513
'fid':'0',
'appType':'15',
'ifTiJiao':'1',
"validate":""
}
cook = {
    'uf':cookies["uf"],
    '_d':cookies["_d"],
    'vc3':cookies["vc3"],
    'UID':cookies["UID"]
}
session.cookies = requests.utils.cookiejar_from_dict(cookies, cookiejar=None, overwrite=True)
r = session.get(url,params=data)
print('位置签到')
print('r:',r.text)
