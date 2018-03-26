#coding=utf8
import tweepy
import urllib
import os
from secrets import *

global exec_dir
exec_dir = '/home/frank/weibo-twitter-sync-bot/'

def download_pic(pic_url,time_stamp):
    file_name = time_stamp + ".jpg"
    os.system('wget ' + pic_url + ' -O ' + exec_dir + file_name)
    return exec_dir + file_name

def send_tweet(tweet_array):
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)
    #api.update_with_media(pic_file,status='test_tweet_with_pic')

    for tweet in tweet_array:
        if tweet[1] == '':#先判断是否带图，如果不带图则直接发送，带图则将图片下载后发送
            print tweet[0]
            api.update_status(tweet[0])
        elif tweet[1] != '':
            pic_file = download_pic(tweet[1],tweet[2])
            print tweet[0]
            print pic_file
            api.update_with_media(pic_file,status=tweet[0])

