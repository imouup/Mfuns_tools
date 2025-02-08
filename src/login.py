import getpass
import time
import sys
sys.path.append('.\\')# 设置sys.path
sys.path.append(r'.\site-packages')
from src.mf_print import mfprint

def login(tab):
    # 跳转到登录页面
    tab.get('https://mfuns.net')

    # 判断是否已经登录
    if bool(tab.ele('.m-img m-avatar',timeout=3.0)) == True:
        mfprint('已经登录了喵~')
    else:
        # 获取用户名和密码
        username = input('请输入你的mfuns账号：')
        password = getpass.getpass("请输入你的密码(密码已隐藏~)：")
        # password = input("请输入你的密码(密码未隐藏~)：")
        # # 最后要记得换成getpass

        # 点击“登录”按钮
        tab.ele('.__button-1cvdmx0-lsmp n-button n-button--primary-type n-button--small-type button signin').click()

        # 定位到账号文本框，获取文本框元素
        login = tab.ele('@autocomplete=username')
            # els用于查找元素，它返回一个ChromiumElement对象，用于操作元素
            # '#user_login'是定位符文本，#意思是按id属性查找元素

        login.input(str(username))

        # 同理输入密码
        passin = tab.ele('@autocomplete=current-password')
        passin.input(str(password))

        # 点击登录
        tab.ele('.__button-1cvdmx0-ilmmp n-button n-button--primary-type n-button--medium-type n-button--block').click()
            # 通过其value属性作为查找条件。@表示按属性名查找
        mfprint('登陆成功了喵！')
        time.sleep(1)
        tab.refresh()

# 注意：这里没有切换模式 若要使用s模式请用tab.change_mode()