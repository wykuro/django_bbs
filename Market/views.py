from User import models
import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, request, HttpResponseRedirect
from Market import models


def market(response):
    username = models.User.objects.get(username=response.user)
    Market_list = models.BBS_goods.objects.all()
    return render(response, 'Market/index.html', {'Market_list': Market_list, 'username': username})


def category1(response):
    username = models.User.objects.get(username=response.user)
    Market_list = models.BBS_goods.objects.filter(category="可食物品")
    return render(response, 'Market/index.html', {'Market_list': Market_list, 'username': username})


def category2(response):
    username = models.User.objects.get(username=response.user)
    Market_list = models.BBS_goods.objects.filter(category="日常用品")
    return render(response, 'Market/index.html', {'Market_list': Market_list, 'username': username})


def category3(response):
    username = models.User.objects.get(username=response.user)
    Market_list = models.BBS_goods.objects.filter(category="体育用品")
    return render(response, 'Market/index.html', {'Market_list': Market_list, 'username': username})


def category4(response):
    username = models.User.objects.get(username=response.user)
    Market_list = models.BBS_goods.objects.filter(category="电子产品")
    return render(response, 'Market/index.html', {'Market_list': Market_list, 'username': username})


def category5(response):
    username = models.User.objects.get(username=response.user)
    Market_list = models.BBS_goods.objects.filter(category="学习用品")
    return render(response, 'Market/index.html', {'Market_list': Market_list, 'username': username})


def category6(response):
    username = models.User.objects.get(username=response.user)
    Market_list = models.BBS_goods.objects.filter(category="其他")
    return render(response, 'Market/index.html', {'Market_list': Market_list, 'username': username})


def item(response, goods_id):
    username = models.User.objects.get(username=response.user)
    market_obj = models.BBS_goods.objects.get(id=goods_id)
    category = market_obj.category
    market_list = models.BBS_goods.objects.filter(category=category)
    return render(response, 'Market/item.html',
                  {'username': username, 'market_obj': market_obj, 'market_list': market_list})


def delete(request, goods_id):
    market_obj = models.BBS_goods.objects.get(id=goods_id)
    market_obj.delete()
    return HttpResponseRedirect("/Market/user_market/")


def search(response):
    username = models.User.objects.get(username=response.user)
    q = response.GET.get('q', '')
    error_msg = ''
    post_list = models.BBS_goods.objects.filter(title__icontains=q)
    if post_list.count() == 0:
        error_msg = "未搜索到相关商品"
    return render(response, 'Market/search.html',
                  {'error_msg': error_msg, 'post_list': post_list, 'username': username})


def user_market(response):
    username = models.User.objects.get(username=response.user)
    marketlist = models.BBS_goods.objects.filter(author=username)
    num_market = marketlist.count()
    return render(response, 'User/Market.html', {'username': username, 'marketlist': marketlist,
                                                 'num_market': num_market})


def market_sub(requset):
    author = models.User.objects.get(username=requset.user)
    models.BBS_goods.objects.create(
        title=requset.POST.get('title'),
        prices=requset.POST.get('prices'),
        time=requset.POST.get('time'),
        tel=requset.POST.get('tel'),
        photo1=requset.FILES.get('photo1'),
        photo2=requset.FILES.get('photo2'),
        photo3=requset.FILES.get('photo3'),
        content=requset.POST.get('content'),
        category=requset.POST.get('category'),
        author=author,
        view_count=0,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    return HttpResponseRedirect("/Market/user_market/")
