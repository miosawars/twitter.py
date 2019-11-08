# -*- coding: utf-8 -*-

import tweepy, config

# 各種キーをセット
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_TOKEN_SECRET

#APIインスタンスを作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#検索キーワード
q = "keyword" #ここに検索キーワードを設定
count = 100

search_results = api.search(q=q, count=count)

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
    user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
    tweet = result.text #ツイートの内容を追加
    time = result.created_at #ツイートの日時を取得
    try:
        api.create_friendship(username) #フォローする
        print(str(username) + "をFollowしました")
    except Exception as e:
        print(e)
