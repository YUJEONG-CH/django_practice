from django.shortcuts import render
import random

# Create your views here.
def index(request):
    #환영하는 메인페이지 보여줌

    names = ['유정', '현정', '우정', '동영', '민우']
    name = random.choice(names)

    context = {
        'name': name,
        'img': 'https://shop4.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop4.daumcdn.net%2Fshophow%2Fp%2FL12406911713.jpg%3Fut%3D20210223040629'
    }

    return render(request, 'index.html', context)


def welcome(request, name):
    #welcome/본인이름 입력 시, 환영인사와 이름을 동시에 보여줌
    #print(name)

    context = {
        'name': name,
        'greetings': [
            '안녕하세요', 'hello', 'guten tag', 'bon jour'
        ],
    }
    return render(request, 'welcome.html', context)