#coding: UTF-8

import twitter, config

def init():
    # 自分のアカウントIDを設定
    my_id = "id"

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET


    return twitter.Twitter(auth=auth), my_id

def follow(t, my_id):
    followers = t.followers.list(screen_name=my_id)
    for fw in followers['users']:
        name = fw['screen_name']
        if fw['following'] == False:
            t.friendships.create(screen_name=name)
            print("@" + str(name) + "さんをフォローしました。")

if __name__ == '__main__':
    tw, my_id = init()
    follow(tw, my_id)
