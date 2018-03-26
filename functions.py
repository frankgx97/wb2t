#!/usr/bin/env python
#coding=utf8
global exec_dir
exec_dir = '/home/frank/weibo-twitter-sync-bot/'

def write_time_stamp(time_stamp):
    file = exec_dir + 'time_stamp.txt'
    with open(file,"w") as f:
        f.write(str(time_stamp))
        f.close()


def read_last_time_stamp():
    file = exec_dir + 'time_stamp.txt'
    with open(file,"r") as f:
        last_time_stamp = f.read()
        f.close()
    return last_time_stamp

def resolve_time(wb_post_time):
    m = wb_post_time[4:7]
    d = wb_post_time[8:10]
    h = wb_post_time[11:13]
    mi = wb_post_time[14:16]
    s = wb_post_time[17:19]
    yr = wb_post_time[26:30]

    if m == 'Jan':
        m = '01'
    elif m == 'Feb':
        m = '02'
    elif m == 'Mar':
        m = '03'
    elif m == 'Apr':
        m = '04'
    elif m == 'May':
        m = '05'
    elif m == 'Jun':
        m = '06'
    elif m == 'Jul':
        m = '07'
    elif m == 'Aug':
        m = '08'
    elif m == 'Sep':
        m = '09'
    elif m == 'Oct':
        m = '10'
    elif m == 'Nov':
        m = '11'
    elif m == 'Dec':
        m = '12'
    else:
        m = '00'

    return yr+m+d+h+mi+s
