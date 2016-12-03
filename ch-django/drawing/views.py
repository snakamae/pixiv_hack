# -*- coding: utf-8 -*-

from django.shortcuts import render
import urllib
import unirest
import json

# URLのv1より後はget処理内に記述する
API_URL = ""
ACCESS_TOKEN = ""
API_HEADER = {"Authorization": ACCESS_TOKEN}


def index(request):
    return render(request, 'drawing/index.html')


# ユーザ投稿作品抽出ビュー
def userworks(request, user_id):
    # クエリで送るパラメータを辞書形式で指定
    query_string = urllib.urlencode("")

    # APIを呼び出してレスポンスオブジェクトを得る
    response = unirest.get(API_URL + "/users/" + user_id + "/works?" + query_string, headers=API_HEADER)
    json_data = response.body

    image_urls = []
    works = json_data["response"]
    for work in works:
        image_urls.append(work["image_urls"]["small"])

    image_json = json.dumps({'image_urls': image_urls})

    # HTTPコードをチェックして200以外だったらエラーということで例外を上げる
    if response.code != 200:
        raise Exception("HTTP Error %d : %s" % (response.code, response.raw_body))

    result = {
        "data": image_json
    }

    return render(request, 'drawing/data_output.html', result)


# ランキング作品抽出ビュー
def ranking(request):
    image_urls = []


    for i in range(1):
        query_string = urllib.urlencode({"mode": "rookie", "page": (i+1)})

        response = unirest.get(API_URL + "/ranking/all?" + query_string, headers=API_HEADER)

        if response.code != 200:
            raise Exception("HTTP Error %d : %s" % (response.code, response.raw_body))

        json_data = response.body
        works = json_data["response"][0]["works"]
        for work in works:
            image_urls.append(work["work"]["image_urls"]["small"])

    image_json = json.dumps({'image_urls': image_urls})

    result = {
        "data": image_json
    }

    return render(request, 'drawing/data_output.html', result)
