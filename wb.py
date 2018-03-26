#coding=utf8
from weibo import APIClient
from secrets import *   #微博和twitter的api key
from tokens import *     #微博授权后的access token
from functions import *
from twitterbot import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

global exec_dir
exec_dir = '/home/frank/weibo-twitter-sync-bot/'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
client.set_access_token(access_token, expires_in)
tl =  client.statuses.user_timeline.get()

tweet_array = []#待发送的推文阵列
last_time_stamp = read_last_time_stamp()
for i,st in enumerate(tl.statuses):
    print i
    print 'content:' 
    print st.text
    #判断是否为转发，如果是则抛弃
    if hasattr(st,'retweeted_status') == True:
        continue
    #判断是否带图，如果是则设置pic_url，反之则将pic_url设为空
    if hasattr(st,'original_pic') == True:
        pic_url = st.original_pic
    else:
        pic_url = ''
    #解析时间
    wb_post_time = st.created_at
    time_stamp = resolve_time(wb_post_time)

    if i == 0 and time_stamp > last_time_stamp:#在第一次循环时将最新的微博时间写入文件中
        write_time_stamp(time_stamp)

    print 'Time:' + time_stamp
    print 'pic-url:' + pic_url
    print '===================='

    tweet = [st.text,pic_url,time_stamp]
    #判断时间差，如果时间正确则加入发送阵列，反之则抓取结束

    if time_stamp > last_time_stamp:
        tweet_array.append(tweet)
    else:
        break
print 'Tweet array:'
print tweet_array
send_tweet(tweet_array)





