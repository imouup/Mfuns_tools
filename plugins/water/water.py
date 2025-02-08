import json
import time
import sys
sys.path.append('.\\') # 设置sys.path
sys.path.append(r'.\site-packages')
from src.createTab import CreateTab
from src.login import login
from src.cookies import getAccessToken
from src.mf_print import mfprint
import requests

# 创建页面
ini_path = None
createtab = CreateTab(ini_path)
createtab.headless(False)
tab = createtab.create()

# 登录
login(tab)
AccessToken = getAccessToken(tab)

def signin():
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
        'Authorization': AccessToken,
        'Origin': 'https://www.mfuns.net',
        'Referer': 'https://www.mfuns.net/',
        'Priority': 'u=1,i',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response =requests.get(url='https://api.mfuns.net/v1/sign/sign',headers=header)
    return response

def findjson(decoded_content):
    start = decoded_content.find('{')
    end = decoded_content.rfind('}')
    return decoded_content[start:end+1]

time.sleep(1)
# 签到
response = signin()

# 获取签到信息
content = response.content
decoded = content.decode('utf-8',errors='ignore')
dict = json.loads(findjson(decoded))
mfprint(dict['msg'])





