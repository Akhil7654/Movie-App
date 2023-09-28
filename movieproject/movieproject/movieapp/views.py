from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.form import movieform
from movieapp.models import movie


# Create your views here.

def index(request):
    obj1=movie.objects.all()
    return render(request,"index.html",{"res":obj1})

def detail(request,movie_id):
    obj2=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{"res2":obj2})

def add_movie(request):
    if request.method=="POST":
        mname=request.POST.get('name')
        mgen = request.POST.get('gen')
        myear = request.POST.get('year')
        mdes = request.POST.get('des')
        mimg=request.FILES['img']
        movies=movie(name=mname,gen=mgen,year=myear,des=mdes,img=mimg)
        movies.save()
        return redirect("/")

    return render(request,"add-movie.html")


def update_movie(request,id):
    Movie= movie.objects.get(id=id)
    Form= movieform(request.POST or None, request.FILES,instance=Movie)
    if Form.is_valid():
        Form.save()
        return redirect("/")
    return render(request,"updateform.html",{"form1":Form,"movie1":Movie})

def delete_movie(request,id):
    if request.method=="POST":
        delete_movies = movie.objects.get(id=id)
        delete_movies.delete()
        return redirect("/")
    return render(request,"delete.html")


