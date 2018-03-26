# coding=utf8
from weibo import APIClient
from secrets import *

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
#url = https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//www.lynx.im/&response_type=code&client_id=1442549166
code = ''
r = client.request_access_token(code)

access_token = r.access_token # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4

print access_token
print expires_in
