# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import urllib
import unirest
import json
from .models import Log
import xml.etree.ElementTree as ET

# URLのv1より後はget処理内に記述する
API_URL = "https://www.bing.com/HPImageArchive.aspx"
BING_URL = "https://www.bing.com"


# ランキング作品抽出ビュー(HIGH解像度)
def image_view(request):
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

    return render(request, 'drawing/render_image.html', result)


# 基本的にAjaxから呼ぶ
def log(request):
    kind = request.GET['kind']
    count = Log.objects.filter(page_kind=kind).count()
    return HttpResponse(count)

