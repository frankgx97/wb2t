# wb2t
Python实现的微博与twitter单向同步工具

## 关于本项目
我在过去一段时间内都使用的是IFTTT的Recipe进行同步。但是IFTTT的同步有些缺陷：

不能判断该条微博是原创还是转发，因此转发的微博也会被同步过去，把时间线弄得一团糟
不能发图，而是将图片以链接的形式替换。访问图片要经过至少两次短连接跳转，体验极差。
为了改善上述两个问题我写了一个简陋的同步程序，用于将新发布的微博同步至twitter。

## 部署
### Docker
按照下面步骤设置相关参数，然后执行
```
docker-compose run wb2t
```
### 手动
#### 新建APP
twitter：https://apps.twitter.com/
微博：http://open.weibo.com/apps

安装依赖
```
sudo -H pip install sinaweibopy
sudo -H pip install tweepy
```
从远程仓库检出代码
```
git clone https://github.com/nyanim/weibo-twitter-sync-bot-public.git
```
配置相关的key及access token
`vim secrects.py`

```
#encoding: utf-8
#twitter 
C_KEY = ""
C_SECRET = ""
A_TOKEN = ""
A_TOKEN_SECRET = ""
 
#weibo
APP_KEY = '' # app key
APP_SECRET = '' # app secret
CALLBACK_URL = '' # callback url
```

微博OAuth认证
`python wb_auth.py`
按照屏幕提示完成认证，屏幕将显示access token和expires in，将这两个值填入tokens.py
`vim tokens.py`

```
#encoding: utf-8
#sinaweibo access token
access_token = ''
expires_in =
```

添加crontab
`crontab -e`
将wb.py设置为按照你想要的频率执行。

脚本第一次执行时会同步最近的5条微博，每次运行时也最多只能同步5条微博。多图的微博只会同步第一张图片。

## 已知存在的问题
twitter有140字的字数限制，但是微博可以超过140字，因此对于超出字数限制的微博可能会发生错误。
twitter api禁止发送相同的内容，但是程序中没有进行查重或捕获异常。
执行的时候如果把输出重定向到文件，就会报UnicodeError: ASCII decoding error: ordinal not in range(128)，但是输出到屏幕没有问题。
执行时需要先将工作目录定位到项目根目录。
之后可能会加入报警功能。正好IFTTT加入了Maker Channel，只要向IFTTT发送一条请求就可以直接把消息推送到手机上，非常方便。

## 用到的开源项目
sinaweibopy
tweepy 