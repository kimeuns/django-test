import random
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from landing.models import Post


def index(request):
    return render(request, "landing/index.html")


def post_create(request):
    if request.method == "GET":
        return render(request, "landing/create.html")

    elif request.method == "POST":

        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.content = request.POST["content"]

        if request.FILES["image"]:
            new_post.head_image = request.FILES["image"]
            
        new_post.save()

        return HttpResponseRedirect("/landing/read-all/")


def post_read_all(request):
    post_list = Post.objects.all()
    context = {
        "posts": post_list,
    }
    return render(request, "landing/read-all.html", context)


def post_read(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, "landing/read.html", context)


def post_update(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            "post": post
        }
        return render(request, "landing/update.html", context)

    elif request.method == "POST":
        target__post = Post.objects.get(id=post_id)
        target__post.title = request.POST["title"]
        target__post.content = request.POST["content"]
        target__post.save()

    return HttpResponseRedirect(f"/landing/read/{post_id}")


def post_delete(request, post_id):
    # if request.method == "GET":
    #     post = Post.objects.get(id=post_id)
    #     context = {
    #         "post": post
    #     }
    #     return render(request, "landing/delete.html", context)

    # elif request.method == "POST":
    target_post = Post.objects.get(id=post_id)
    target_post.delete()
    
    return HttpResponseRedirect("/landing/read-all/")


def temp_test(request):
    context = {
        "weather": "맑음",
        "temperature": 15,
        "weather_data": {
            "weather": "흐림",
            "temperature": 10
        },
        "football_players": [
            {
                "name": "son",
                "team": "토트넘"
            },
            {
                "name": "lee",
                "team": "abc"
            },
            {
                "name": "kang",
                "team": "fgtew"
            }
        ],
    }
    return render(request, "landing/temptest.html", context)
