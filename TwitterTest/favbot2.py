# -*- coding: utf-8 -*-

import config
import tweepy
import time

# TwitterAPIの認証データを取得して認証
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

follow_count = 0
loop_out = False
for loop_count in range(7):
    print("----------------------------------")
    print(str(loop_count + 1) + "回目のループ開始！")
    print("----------------------------------")
    if loop_count == 0:
        query = "エレキベース"
    elif loop_count == 1:
        query = "ウッドベース"
    elif loop_count == 2:
        query = "ベーシスト"
    elif loop_count == 3:
        query = "ジャズベース"
    elif loop_count == 4:
        query = "コントラバス"
    elif loop_count == 5:
        query = "軽音"
    elif loop_count == 6:
        query = "フレットレス"
    elif loop_count == 7:
        query = "ダブルベース"
    #検索はMax100人みたい。検索結果に出てきたアカウント数が上限となる。
    search_count = 100
    my_screen_name = "twitter_account_name" #自分のアカウント名

    favorite_count = 0
    check_count = 0
    search_results = api.search(q=query, count=search_count)
    for result in search_results:
        # ふぁぼ回数が特定人数以上になったらループ抜けて処理終了。
        if favorite_count > 500:
            loop_out = True
            break
        tweet_id = result.id
        check_count += 1
        print("-----------------------------------------")
        print("[" + str(loop_count + 1) + "ループ目] 現状" + str(favorite_count) + "ツイートを新規いいね。" + str(check_count) + "個目のツイート(tweet_id:" + str(tweet_id) + ")をチェック開始！")


        try:
            api.create_favorite(tweet_id)
            print(tweet_id, ":", "いいねしました")
            favorite_count += 1

        except:
            print(tweet_id, ":", "はいいね出来ませんでした。すでにいいねしているか、ブロックされているかも？")

    print("----------------------------------")
    print(str(loop_count + 1) + "回目のループが終了しました")
    print("----------------------------------")
    # いいね上限になったらループ抜ける
    if loop_out:
        break
    # アクセス連続しすぎるとやばいかもだから5分待つ（5分待つことで、153APIアクセス/5分 = 459APIアクセス/15分でAPIアクセス上限に引っかからないはず。）
    print("5分待ちます")
    time.sleep(300)
