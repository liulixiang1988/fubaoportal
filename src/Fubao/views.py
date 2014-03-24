from django.shortcuts import render

# Create your views here.


def home(request):
    title = '福宝'
    return render(request, 'Fubao/index.html', locals())
