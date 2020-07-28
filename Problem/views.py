from User import models
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Problem import models
from django.urls import reverse


def problem(response):
    username = models.User.objects.get(username=response.user)
    pro_list = models.BBS_problems.objects.all()
    pro_list2 = models.BBS_problems.objects.all().order_by('-created_at')[:5]
    pro_list3 = models.BBS_problems.objects.all().order_by('-view_count')[:5]
    return render(response, 'Problem/index.html',
                  {'username': username, 'pro_list': pro_list, 'pro_list2': pro_list2, 'pro_list3': pro_list3})


def item(response, Problem_id):
    username = models.User.objects.get(username=response.user)
    Problem_obj = models.BBS_problems.objects.get(id=Problem_id)
    comment_list = models.BBS_comments_problems.objects.filter(flag_id=Problem_id)
    user_id = Problem_obj.author_id
    author_obj1 = models.User.objects.get(id=user_id)
    author_obj = models.User_user.objects.get(user_id=user_id)
    Problem_obj.view_count = Problem_obj.view_count + 1
    Problem_obj.save()
    return render(response, 'Problem/item.html',
                  {'username': username, 'comment_list': comment_list, 'Problem_obj': Problem_obj,
                   'author_obj': author_obj, 'author_obj1': author_obj1})


def comment_sub(response):
    author = models.User.objects.get(username=response.user)
    models.BBS_comments_problems.objects.create(
        comment=response.POST.get('comment'),
        author=author,
        flag_id=response.POST.get('flag_id'),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        view_count=0,
    )
    flag_id = response.POST.get('flag_id')
    return HttpResponseRedirect(reverse('detail_pm', args=(flag_id,)))


def delete(request, problem_id):
    problem_obj = models.BBS_problems.objects.get(id=problem_id)
    problem_obj.delete()
    return HttpResponseRedirect("/Problem/user_problem/")


def problem_sub(requset):
    author = models.User.objects.get(username=requset.user)
    models.BBS_problems.objects.create(
        title=requset.POST.get('title'),
        content=requset.POST.get('content'),
        author=author,
        ranking=0,
        view_count=0,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    return HttpResponseRedirect("/Problem/user_problem/")


def user_problem(response):
    username = models.User.objects.get(username=response.user)
    problemlist = models.BBS_problems.objects.filter(author=username)
    num_problem = problemlist.count()
    return render(response, 'User/Problem.html', {'username': username, 'problemlist': problemlist,
                                                  'num_problem': num_problem})
