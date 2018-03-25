from django.shortcuts import render,HttpResponse

# Create your views here.



def timer(req):

    import datetime


    t_obj=datetime.datetime.now()

    l=[111,222,333]
    d={"name":"egon","age":35}


    return render(req,"timer.html",{"t":t_obj,"li":l,"dic":d})