import json
import requests
import re
import time
#uid = 152373457
#cpi = 153922417
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
img = "cbf1b18ab127ff3e8195a657f8f81863.jpg"
def token(cookies):  # 获取上传图片用的token
    url = 'https://pan-yz.chaoxing.com/api/token/uservalid'
    res = requests.get(url, headers=headers,cookies=cookies)
    tokendict = json.loads(res.text)
    return tokendict['_token']
def upload(cookies):  # 上传图片
    
	url = 'https://pan-yz.chaoxing.com/upload'
    
	files = {'file': (img, open(img, 'rb'),'image/webp,image/*',), }
	res = requests.post(url, data={'puid': cookies['UID'], '_token':token(cookies)},files=files,headers=headers)
	resdict = json.loads(res.text)
	return resdict['objectId']
#获取用户姓名


        

    
