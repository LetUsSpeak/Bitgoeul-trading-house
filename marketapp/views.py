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
    with open('private/token.txt', encoding='utf-8') as txtfile:
        for row in txtfile.readlines():
            token = row
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": "Bearer " + token
    }

    data = {
        "template_object": json.dumps({
            "object_type": "feed",
            "content": {
                "title": "🎊 빛고을상회 🎊 에 오신 것을 환영합니다",
                "description": "앞으로 자주 만나요!! 더 발전해가겠습니다",
                "image_url": "https://postfiles.pstatic.net/MjAyMTEwMTNfNjQg/MDAxNjM0MDU4MTQzMjA5.yep2OdKvVyNw-Rrwl3tJSmVi3o5QFX3pOzOFRHj7R5Mg.-7elzcIyP1fFgZfeHW2e5TY8Iwa8O_2125liNTqbm_wg.PNG.polkmn249/2021-10-13-01-49-05.png?type=w966",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
            "buttons": [
                {
                    "title": "웹으로 이동",
                    "link": {
                        "web_url": "http://www.daum.net",
                        "mobile_web_url": "http://m.daum.net"
                    }}

            ]
        })
    }

    response = requests.post(url, headers=headers, data=data)

    return render(request, 'marketapp/landing.html')
