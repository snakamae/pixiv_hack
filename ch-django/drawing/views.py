# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
import urllib
import unirest
import json
from .models import Log
import xml.etree.ElementTree as ET

# URLのv1より後はget処理内に記述する
API_URL = "https://www.bing.com/HPImageArchive.aspx"
BING_URL = "https://www.bing.com"

# ユーザ投稿作品抽出ビュー
def userworks(request, user_id):
    # クエリで送るパラメータを辞書形式で指定
    query_string = urllib.urlencode({"format": "xml", "mkt": "ja-JP", "n": 8})

    # APIを呼び出してレスポンスオブジェクトを得る
    response = unirest.get(API_URL + "?" + query_string)
    xml_data = response.body
    root = ET.fromstring(xml_data)

    image_urls = []
    for i in root:
        image_url = i[3].text
        image_url = API_URL + image_url
        image_urls.append(image_url)

    image_json = json.dumps({'image_urls': image_urls})

    # HTTPコードをチェックして200以外だったらエラーということで例外を上げる
    if response.code != 200:
        raise Exception("HTTP Error %d : %s" % (response.code, response.raw_body))

    result = {
        "data": image_json
    }
    print image_json

    return render(request, 'drawing/index.html', result)


# ランキング作品抽出ビュー(HIGH解像度)
def ranking_high(request, kind):
    # クエリで送るパラメータを辞書形式で指定
    query_string = urllib.urlencode({"format": "xml", "mkt": "ja-JP", "n": 20})

    # APIを呼び出してレスポンスオブジェクトを得る
    response = unirest.get(API_URL + "?" + query_string)
    xml_data = response.body
    root = ET.fromstring(xml_data)

    image_urls = []
    for idx, obj in enumerate(root):
        image_url = obj[3].text
        image_url = str(BING_URL) + str(image_url)
        if idx < len(root) - 1:
            image_urls.append(image_url)

    image_json = json.dumps({'image_urls': image_urls})

    # HTTPコードをチェックして200以外だったらエラーということで例外を上げる
    if response.code != 200:
        raise Exception("HTTP Error %d : %s" % (response.code, response.raw_body))

    result = {
        "data": image_json
    }

    return render(request, 'drawing/index_high.html', result)


# ランキング作品抽出ビュー(MID解像度)
def ranking_mid(request, kind):
    image_urls = []

    Log.objects.create(page_kind="ranking")
    for i in range(2):
        query_string = urllib.urlencode({"mode": kind, "page": (i + 1)})
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
    return render(request, 'drawing/index_mid.html', result)


# ランキング作品抽出ビュー(LOW解像度)
def ranking_low(request, kind):
    image_urls = []

    Log.objects.create(page_kind="ranking")
    for i in range(2):
        query_string = urllib.urlencode({"mode": kind, "page": (i + 1)})
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
    return render(request, 'drawing/index_low.html', result)


# 基本的にAjaxから呼ぶ
def log(request):
    kind = request.GET['kind']
    count = Log.objects.filter(page_kind=kind).count()
    return HttpResponse(count)


# デモ用
def demo_view(request):
    return render(request, 'demo/demo_page.html')
