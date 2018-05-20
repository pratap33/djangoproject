from django.shortcuts import render
from django.views.generic import View
from .models import user1
class Homepage(View):
    def get(self,request):
        return render(request, 'homepage.html')
class Loginpage(View):
    def get(self,request):
        return render(request, 'loginpage.html')
class Loginpage1(View):
    def get(self,request):
        return render(request, 'loginpage1.html')
class Showpage(View):
    def post(self,request):
        return render(request, 'showpage.html')
def insert(request):
    try:
         rec=user1.objects.filter(uname=request.GET['t1'],pwrd=request.GET['t2'])
    except user1.DoesNotExist :
        return render(request, 'errorpage.html')
    else:
        return render(request, 'showpage.html', {'records': rec})
def function(request):
    try:
        rec = user1.objects.filter(uname=request.GET['t1'], pwrd=request.GET['t2'])
    except user1.DoesNotExist :
        return render(request, 'errorpage1.html')
    else:
        return render(request, 'showpage1.html', {'records': rec})
def split(request):
    rec = user1.objects.filter(uname=request.GET['t6'])
    ('hello':rec)
    for rec in hello:
        a = rec.actbal
    fname = request.POST['t3']
    samt= int(request.POST['t4'])
   # fnum = int(request.POST['t5'])
    user1.objects.filter(uname=request.POST['t6']).update(splitbal=samt,paidto=fname)
    return render(request, 'errorpage1.html', {'records': rec})