import base64
from urllib.parse import unquote
import json
import requests

def getCookies(tab,path):
    '''
    该函数用于下载Cookies并保存到data/userinfo/cookies.json内

    :param tab: 传入浏览器标签页对象
    :param path: 传入文件保存地址
    :return: None
    '''
    cookies_ls = tab.cookies()
    ckls = []
    for cookie_dic in cookies_ls:
        for key in cookie_dic:
            cookie_dic[key] = unquote(cookie_dic[key])
        ckls.append(cookie_dic)

    with open(path, 'w', encoding='UTF8') as cookies_json:
        json.dump(ckls, cookies_json, ensure_ascii=False, indent=4)


def getUserinfo(tab,path):
    '''
    该函数用于下载&保存Cookies中的userinfo并返回userinfo的字典

    :param tab: 传入浏览器标签页对象
    :param path: 传入文件保存地址
    :return: userinfo的字典
    '''
    cookies_ls = tab.cookies()
    for i in cookies_ls:
        if i['name'] == 'userInfo':
            value = unquote(i['value'])
            json_value = json.loads(value)
            with open(path,'w',encoding='UTF8') as userinfo:
                json.dump(json_value,userinfo,ensure_ascii=False,indent=4)
            return json_value

# 通过页面获取AccessToken(旧)
def getAccessToken(tab):
    cookie = list(tab.cookies())
    for item in cookie:
        if item['name'] == 'access_token':
            access_token = unquote(item['value'])
    access_token = access_token.strip('\"')
    return access_token

# 通过登录的方式获取
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
    print(response.json())