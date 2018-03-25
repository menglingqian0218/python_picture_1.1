from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


import datetime



def index(request):

    timer=datetime.datetime.now()
    return HttpResponse(timer)


def login_in(request):

    if request.method=="POST":
        print("=============",request.POST)
        username=request.POST.get("user")
        password=request.POST.get("pwd")

        if username=="yuan" and password=="123":
            return redirect("/back/")

    return render(request,"login_in.html")




def year_2004(request):

    return HttpResponse("2004")


def year2(request):
    return HttpResponse("ok")

def year(request,year):

    return HttpResponse(year)

def year_month(requset,months,year):

    return HttpResponse("year: %s month: %s"%(year,months))



def sendByget(request):
    print("====GET:",request.GET)

    return HttpResponse("ok")


def back(request):

    name="yuan"
    return render(request,"back.html",locals())


