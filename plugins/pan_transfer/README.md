<div align = "center">
<img src="https://pic-oss.mouup.top/pic/2025/01/f27fbbe4aade501268117c96cc504940.png" alt="pan_icon" style="vertical-align: middle;border-radius: 25%;"> 
<h1>PanTransfer</h1>
<h5>网盘外链转直链工具</h5>
</div>
<br>

## 💡这是什么
这是Mftools工具集的一部分，可以自动将你在Mfuns中投稿的外链视频下载到本地重新上传转为直链


## ✅用前必看
* 脚本存在不稳定性，**请时刻留意脚本行为，出现问题时及时停止脚本**（可以关闭脚本的浏览器/Ctrl+C停止脚本）
* 所有转直链的视频都会下载在Mftools根目录下的`data/pan_transfer/download`目录内，如果脚本出现错误操作，可以在此处找回视频重新手动上传
* 若出现意外错误，导致视频未能正确下载，但是已经写入`data/pan_transfer/log.json`，可以手动删除/修改记录
* **千万不要删掉`data/pan_transfer/log.json`！！！**
* 如果Chrome密码窗口弹出导致脚本中断，可以重新运行脚本
  
<br>


## ✨如何使用

### 开始前：
按照[这里的指引](https://github.com/imouup/Mfuns_tools/blob/main/README.md)准备好Mftools



### 1.Mftools脚本成功运行后输入序号1，选择`网盘外链转直链`

```
 _      _____ _____  ____  ____  _     ____
/ \__/|/    //__ __\/  _ \/  _ \/ \   / ___\
| |\/|||  __\  / \  | / \|| / \|| |   |    \
| |  ||| |     | |  | \_/|| \_/|| |_/\\___ |
\_/  \|\_/     \_/  \____/\____/\____/\____/

Checking~
Version:0.1.0
虚拟环境已激活，当前使用: G:\Project\Mfuns_tools\.venv\Scripts\python.exe

【Mftools】功能列表如下：
1.网盘外链转直链
...(没有更多了)...

【Mftools】请选择功能:1
```

<br>

### 2.脚本自动检索用户视频以及其中使用了nya盘外链的视频
```
【Mftools】正在登录~
【Mftools】已经登录了喵~
【Mftools】请不要关闭弹出的浏览器窗口!
【Mftools】脚本不稳定，请随时留意脚本在浏览器中的操作 ╰(￣ω￣ｏ)
【Mftools】你的UID为2333333，看看有没有登录错了喵~
【Mftools】开始检索你上传的视频（￣︶￣）↗
【Mftools】Processing: 100%|███████████████| 66/66 [00:19<00:00,  3.45it/s]
【Mftools】总共检索到47个视频
【Mftools】开始查找使用nya盘外链的视频~
【Mftools】Processing: 100%|███████████████| 47/47 [00:04<00:00,  9.93it/s]
【Mftools】其中有23个使用Nya盘的视频
```

<br>

### 3.在输出的表格中选择你需要转换的视频
#### ✅你可以按照以下任意方式输入：
  - 直接回车或输入0，所有视频都会被尝试转直链
  - 输入单个序号或mv号，只有指定的视频会被转为直链  `例如：1 或 mv35124`
  - 输入多个序号或mv号，用英文逗号分隔 `例如：1,2,3`

#### ⚠️需要注意的是：
  - 逗号必须是英文逗号!
  - 序号和mv号可以混用

```
【Mftools】请输入你希望重新上传以转为直链的视频的【序号】或【mv号】
【Mftools】你可以：
【Mftools】（1）直接回车或输入0，所有视频都会被尝试转直链
【Mftools】或者：
【Mftools】（2）输入单个序号或mv号[例如：1 或 mv35124]，只有指定的视频会被转为直链
【Mftools】（3）输入多个序号或mv号，用英文逗号分隔[例如：1,2,3,]
【Mftools】注意：序号和mv号可以混用；逗号必须是英文逗号!
【Mftools】请输入需要转直链的视频: 7
```

#### ✨Tips: 这里可以选择是否保留外链视频，若保留，直链视频将作为P2
```
【Mftools】请问是否需要保留外链视频（直链作为P2） [Y/N](默认保留):
```

#### 💡历史记录检测
脚本会在`log.json`文件中记录对文件的历史操作，如果发现某个被选中的视频已经转过一次直链，将会提示以下内容：
```
【Mftools】注意：以下视频已经转过直链啦，不过当时保留了外链作为分P：
【Mftools】|序号 |  mv号   | 标题
【Mftools】   1   mv22565   xxxxxxxx
```

* 若你选择保留外链作为分P，会直接提示`将不再对它们进行操作`
* 若不保留外链，你可以选择：
  * A. 不操作
  * B. 同时删除改视频的外链分P

⚠️ 注意：此处默认选项为不操作



<br>

### 4. 脚本自动开始下载视频
```
【Mftools】开始下载: mv34048  【搬运】恶之三部曲   feat.悪ノP，鏡音リン，鏡音レン
【Mftools】Downloading: 100%|████████████████| 9/9 [00:10<00:00,  1.21s/MB]
【Mftools】Downloading: 100%|████████████████| 7/7 [00:12<00:00,  1.78s/MB]
【Mftools】Downloading: 100%|████████████████| 7/7 [00:11<00:00,  1.61s/MB]
【Mftools】mv34048  【搬运】恶之三部曲   feat.悪ノP，鏡音リン，鏡音レン 下载完成~
```

<br>

#### 🔶此时可能会遇到以下几种错误
##### 1.10053错误
```
  【Mftools】开始下载: mv34048  【搬运】恶之三部曲   feat.悪ノP，鏡音リン，鏡音レン
   HTTPSConnectionPool(host='pan.nyaku.moe', port=443): Max retries exceeded with url: /f/BY0Hn/%E6%81%B6%E4%B9%8B%E5%A8%98.mp4 (Caused by ProtocolError('Connection aborted.', ConnectionAbortedError(10053, '你的主机中的软件中止了一个已建立的连接。', None, 10053, None)))
```
##### 💡出现的可能原因：网络问题，连接超时
* Nya盘走了Cloudflare的CDN，在部分地区部分时间段可能会连接超时

##### ✅解决办法：设置代理后重新运行脚本
* 编辑目录`plugins/pan_transfer`下的`config.json`文件，加入以下内容：
  
  ```
  {
  "proxies" :{
  "http": "http://<proxy server>",
  "https": "http://<proxy server>"
    }
  }
  ```
* 其中的`<proxy server>`请改为你自己的代理服务器地址


##### 2.外链文件不存在
```
外链文件不存在,早期使用Mfvideo的外链视频已丢失＞﹏＜，肥肠抱歉 ≧ ﹏ ≦
```
非常抱歉≧ ﹏ ≦，早期使用mfvideo的外链视频由于看管不善，已经被微软清空了 orz

<br>

### 5.上传文件
⚠️ 注意： 在进行该步骤时请留意脚本在浏览器中的操作，若出现问题请及时中止脚本！！！

（进度条和文字位置偏移是正常现象）
```
【Mftools】开始上传 mv34048 【搬运】恶之三部曲   feat.悪ノP，鏡音リン，鏡音レン
开始上传P1
【Mftools】正在上传
100%|████████████████████████████████████| 100/100 [00:08<00:00, 11.62it/s]
【Mftools】请稍等片刻，正在确认是否已经上传完成~
100%|████████████████████████████████████| 100/100 [00:12<00:00,  8.14it/s]
【Mftools】上传成功
【Mftools】操作完成，请去检查一下有没有问题吧
```

<br>

### End
```
【Mftools】请问还需要进行其它操作吗？[Y/N]:
```
选择Y将回到功能列表处

---

## 关于log.json
* 这是日志文件，非常重要，请不要删除！！！
* 文件位置`data/pan_transfer/log.json`
* 文件内容：
  ```
     "34048": {
        "mvid": "34048",
        "conid": 116250,
        "title": "【搬运】恶之三部曲   feat.悪ノP，鏡音リン，鏡音レン",
        "retain_ex_link": true
    }
  ```
  * 每个视频对应的键值对以mv号为键 `例如"34048"`
  * `mvid`: mv号
  * `conid`: 稿件号
  * `title`: 标题
  * `retain_ex_link`: 是否保留外链作为分P