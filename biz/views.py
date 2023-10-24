from django.shortcuts import render

# Create your views here.
def biz_home(request):
    return render(request, 'biz_home.html', {})