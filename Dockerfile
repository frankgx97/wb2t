FROM python:2.7-alpine3.7

WORKDIR /home/frank/weibo-twitter-sync-bot/

COPY . .

RUN pip install -r requirements.txt

CMD python /home/frank/weibo-twitter-sync-bot/wb.py