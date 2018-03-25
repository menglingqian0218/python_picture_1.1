from django.shortcuts import render,redirect
from book.models import *
# Create your views here.


def index(request):

    all_book_list=Book.objects.all()    #  [obj1,obj2,obj3]
    if request.method=="POST":
        all_book_list=Book.objects.filter(title__contains="")
    return render(request,"index.html",{"all_book_list":all_book_list})


def addBook(request):

    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        author=request.POST.get("author")
        publish=request.POST.get("publish")

        print("===========",request.POST)
        # 添加数据库

        Book.objects.create(title=title,price=price,author=author,publiosh=publish)

        return redirect("/index/")

    return render(request,"addBook.html")



def delBook(request):
    id=request.GET.get("id")
    Book.objects.filter(id=id).delete()

    return redirect("/index/")


def edit(request):


    id=4

    Book.objects.filter(id=id).update(title="Yuan")
    return redirect("/index/")
