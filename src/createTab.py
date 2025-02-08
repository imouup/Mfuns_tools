from DrissionPage.common import Settings
from DrissionPage import Chromium
import sys
sys.path.append('.\\')# 设置sys.path
sys.path.append(r'.\site-packages')
from DrissionPage import ChromiumOptions
from src.file_store import getPath


class CreateTab():
    def __init__(self,ini_path,dir_num=0):
        # 设置语言
        Settings.set_language('zh_cn')

        # 创建配置对象,设置隐藏浏览器界面
        self.co = ChromiumOptions(ini_path=ini_path).set_paths(local_port=9100,user_data_path=r'.\data\userdata')
        self.co.set_pref('credentials_enable_service', False)
        self.co.set_pref('profile.password_manager_enabled', False)
        self.co.set_argument('--hide-crash-restore-bubble')
        # self.co.set_browser_path(r'.\data\Chrome\chrome.exe') # 取消注释后使用data目录下的便携式Chrome，你也可以改成其他浏览器的路径

    def headless(self,TorF):
        self.co.headless(TorF)

    def create(self):
        # 启动或接管浏览器，并创建标签页对象
        tab = Chromium(addr_or_opts=self.co).latest_tab
        return tab

    def newtab(self):
        newBrowser = Chromium(addr_or_opts=self.co)
        tab = newBrowser.new_tab()
        return tab

