from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm
# Create your views here.

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    print("*****")
    print(request.method)
    print(request.POST)
    print("*****")

    if request.method =='POST':#post요청
        form = PostForm(request.POST)

        if form.is_valid():
            #result = form.save()
            lotto= form.save(commit=False) #false: github에서의 commit
            lotto.generate()
            #form.save(commit=True) #github에서의 push
            return redirect('index')
    else: #get요청
        form = PostForm() # 상단 from .forms import PostForm 추가
        return render(request, "lotto/form.html", {"form": form})

def detail(request,lottokey):
        lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
        return render(request, "lotto/detail.html", {"lotto":lotto})
