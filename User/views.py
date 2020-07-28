from django.views.generic import View
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json
from django.contrib import auth
from User import models
from django.contrib.auth import logout
import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, request, HttpResponseRedirect


def home(response):
    username = models.User.objects.get(username=response.user)
    return render(response, 'index.html', {'username': username})


def user(response):
    username = models.User.objects.get(username=response.user)
    user_id = username.id
    user_list = models.User_user.objects.filter(user_id=user_id)
    user_num = user_list.count()
    if user_num:
        user_obj = models.User_user.objects.get(user_id=user_id)
        return render(response, 'User/index.html', {'user_obj': user_obj, 'username': username})
    else:
        msg = "点击完善个人信息"
        return render(response, 'User/index.html', {'msg': msg, 'username': username})


# 创建验证码
def captcha():
    hashkey = CaptchaStore.generate_key()  # 验证码答案
    image_url = captcha_image_url(hashkey)  # 验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha


# 刷新验证码
def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')


# 验证验证码
def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            if get_captcha.response == captchaStr.lower():  # 如果验证码匹配
                return True
        except:
            return False
    else:
        return False


class IndexView(View):
    def get(self, request):
        hashkey = CaptchaStore.generate_key()  # 验证码答案
        image_url = captcha_image_url(hashkey)  # 验证码地址
        captcha = {'hashkey': hashkey, 'image_url': image_url}
        return render(request, "login.html", locals())

    def post(self, request):
        number = request.POST.get('number')
        password = request.POST.get('password')
        user = auth.authenticate(username=number, password=password)
        # 验证用户名和密码，验证通过的话，返回user对象
        if user:
            # 验证成功 登陆
            # auth.login(request, user)
            flag1 = 1
        else:
            flag1 = 0
        capt = request.POST.get("captcha", None)  # 用户提交的验证码
        key = request.POST.get("hashkey", None)  # 验证码答案
        if jarge_captcha(capt, key):
            flag2 = 1
        else:
            flag2 = 0
        type1 = "用户名或密码错误"
        type2 = "验证码错误"
        if flag1 == 1 and flag2 == 1:
            auth.login(request, user)
            return HttpResponseRedirect("/home/")
        if flag1 == 0:
            return render(request, 'login.html', {'type1': type1})
        if flag2 == 0:
            return render(request, 'login.html', {'type2': type2})


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/#/")


class register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        password1 == password2
        username = request.POST.get('username')
        u = models.User.objects.filter(username=username).first()
        if u:
            msg = "该学号已存在"
            return render(request, 'register.html', {'msg': msg})
        else:
            models.User.objects.create_user(
                username=username,
                password=request.POST.get('password1'),
            )
        return HttpResponseRedirect("/#/")


class create(View):
    def get(self, request):
        username = models.User.objects.get(username=request.user)
        return render(request, 'User/create.html', {'username': username})

    def post(self, request):
        number = request.POST.get('number')
        u = models.User_user.objects.filter(number=number).first()
        if u:
            msg = "该昵称已存在"
            username = models.User.objects.get(username=request.user)
            return render(request, 'User/create.html', {'msg': msg, 'username': username})
        else:
            user = models.User.objects.get(username=request.user)
            models.User_user.objects.create(
                user=user,
                number=number,
                sex=request.POST.get('sex'),
                dept=request.POST.get('dept'),
                classs=request.POST.get('classs'),
                tel=request.POST.get('tel'),
            )
        return HttpResponseRedirect("/User/")


class update(View):
    def get(self, request):
        username = models.User.objects.get(username=request.user)
        user_id = username.id
        user_list = models.User_user.objects.filter(user_id=user_id)
        user_num = user_list.count()
        if user_num:
            return render(request, 'User/update.html', {'username': username})
        else:
            msg = "点击完善个人信息"
            return render(request, 'User/index.html', {'msg': msg, 'username': username})

    def post(self, request):
        number = request.POST.get('number')
        u = models.User_user.objects.filter(number=number).first()
        if u:
            username = models.User.objects.get(username=request.user)
            msg = "该昵称已存在"
            return render(request, 'User/update.html', {'username': username, 'msg': msg})
        else:
            user = models.User.objects.get(username=request.user)
            user_id = user.id
            user_obj = models.User_user.objects.get(user_id=user_id)
            user_obj.number = number
            user_obj.sex = request.POST.get('sex')
            user_obj.dept = request.POST.get('dept')
            user_obj.classs = request.POST.get('classs')
            user_obj.tel = request.POST.get('tel')
            user_obj.save()
        return HttpResponseRedirect("/User/")
