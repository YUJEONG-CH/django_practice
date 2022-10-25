from django.shortcuts import render
import random

# Create your views here.
def index(request):

    return render(request, "index.html")

def todaymenu(request):
    menu_list = [
        {"name": "김치찌개", "src": "https://cdn.shopify.com/s/files/1/0585/8495/7094/products/main_820b4384-e7f3-41e0-996a-27f192a9f69a.jpg?v=1653695416"},
        {"name": "된장찌개", "src": "https://m.cj.co.kr/images/theKitchen/PHON/0000002053/0000008089/0000002053.jpg"},
        {"name": "삼겹살", "src": "https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg"},

    ]
    context = {
        "menu": random.choice(menu_list)
    }

    return render(request, "todaymenu.html", context)

def lotto(request):
    #로또 번호 6개를 5번 뽑음
    lotto_list = []
    for _ in range(5):
        lotto = random.sample(range(1,46),6)
        lotto_list.append(lotto)

    context = {
        "lotto_list": lotto_list,
    }

    return render(request, 'lotto.html', context)