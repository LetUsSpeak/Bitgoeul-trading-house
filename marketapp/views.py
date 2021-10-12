import json

import requests
from django.shortcuts import render


# Create your views here.


def landing(request):
    return render(
        request,
        'marketapp/landing.html'
    )


def metaverse(request):
    return render(
        request,
        'marketapp/metaverse.html'
    )


def kakao(request):
    with open('data/token.txt', encoding='utf-8') as txtfile:
        for row in txtfile.readlines():
            token = row
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": "Bearer " + token
    }

    data = {
        "template_object": json.dumps({"object_type": "text",
                                       "text": "🎊 빛고을상회 🎊 에 오신 것을 환영합니다",
                                       "link": {
                                           "web_url": "http://127.0.0.1:9000/"
                                       }
                                       })
    }
    response = requests.post(url, headers=headers, data=data)

    return render(request, 'marketapp/landing.html')
