import base64
import datetime
import hashlib
import hmac
import json
import requests
from datetime import datetime
from zoneinfo import ZoneInfo


# 定义函数获取 AccessToken
def getAccessToken2(account,password):
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Authorization': None,
        'Content-Type': 'application/json',
        'Origin': 'https://www.mfuns.net',
        'Referer': 'https://www.mfuns.net/',
        'Priority': 'u=1,i',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    json_data = {
        'account': account,
        'password': password,
    }

    response = requests.post('https://api.mfuns.net/v1/auth/login', headers=headers, json=json_data)

    # 提取json
    content = response.content
    decoded = content.decode('utf-8', errors='ignore')
    start = decoded.find('{')
    end = decoded.rfind('}')
    json_res = decoded[start:end + 1]
    dict = json.loads(json_res)
    access_token = dict['data']['access_token']
    return access_token

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

# 消息发送
def feishu_notice(msg,bot_secret,webhook):
    tz = ZoneInfo('Asia/Shanghai')
    now = datetime.now(tz)
    timestamp = int(now.timestamp())
    secret = bot_secret
    # 生成认证码
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    hmacsign = hmac.new(string_to_sign.encode('utf-8'),digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(hmacsign).decode('utf-8')

    # 组合json
    json_data = {
        'timestamp': str(timestamp),
        'sign': signature,
        'msg_type': 'post',
        'content': {
            'post':{
                'zh_cn':{
                    'title': 'Mfuns自动签到',
                    'content':  [
                        [{
                        'tag': 'text',
                        'text': f'{msg}\n'
                    },{
                        'tag': 'text',
                        'text': f'时间：{now.strftime("%Y-%m-%d %H:%M:%S")}'
                    }]
                    ]
            }
        }
    }
    }

    header = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url=webhook, json=json_data, headers=header)

# 主代码
# 加载配置
with open("config.json") as f:
    config = json.load(f)
account = config['account']
password = config['password']
feishu_bot_secret = config['feishu_bot_secret']
feishu_webhook = config['feishu_webhook']
AccessToken = getAccessToken2(account,password)

#签到
response = signin()

# 获取签到信息
content = response.content
decoded = content.decode('utf-8',errors='ignore')
dict = json.loads(findjson(decoded))
print(dict['msg'])
feishu_notice(dict['msg'],feishu_bot_secret,feishu_webhook)

