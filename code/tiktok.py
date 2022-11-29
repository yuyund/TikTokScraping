from TikTokApi import api,TikTokApi
import requests
from pprint import pprint
from time import sleep
import spread
from datetime import datetime


# "更新日時",
# "フォロワー",
# "いいね",
# "コメント",
# "シェア",
# "投稿日時"


## TestData
# urls = ["https://www.tiktok.com/@dreaminghouse168/video/7125347875155873029?is_copy_url=1&is_from_webapp=v1",
#         "https://google.com",
#         "https://www.tiktok.com/@_.luv83._/video/7120908597738917121?is_copy_url=1&is_from_webapp=v1",
#         "https://www.tiktok.com/@chudung0030/video/7125258363784613166?is_copy_url=1&is_from_webapp=v1"]

def create_data(urls,verify_fp=""):
    if urls:
        with TikTokApi(custom_verify_fp=verify_fp) as api:
            return_list = []
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for url in urls:
                sleep(3)
                try:
                    video = api.video(url=url).info()
                    v = video["stats"]
                    u = video["authorStats"]
                    t = video["createTime"]
                    diggCount = v["diggCount"]
                    shareCount = v["shareCount"]
                    commentCount = v["commentCount"]
                    playCount = v["playCount"]
                    followerCount = u["followerCount"]
                    create_time = unix_to_date(int(t))
                    return_list += [[now,followerCount,diggCount,commentCount,shareCount,playCount,create_time]]
                except Exception:
                    return_list += [[None]]
            return return_list
def unix_to_date(u_time):
    date = datetime.fromtimestamp(u_time).strftime("%Y-%m-%d %H:%M:%S")
    return date
