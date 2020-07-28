from User import models
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Project import models
from django.urls import reverse


def project(response):
    username = models.User.objects.get(username=response.user)
    pro_list = models.BBS_projects.objects.all()
    pro_list2 = models.BBS_projects.objects.all().order_by('-created_at')[:5]
    pro_list3 = models.BBS_projects.objects.all().order_by('-view_count')[:5]
    return render(response, 'Project/index.html',
                  {'username': username, 'pro_list': pro_list, 'pro_list2': pro_list2, 'pro_list3': pro_list3})


def item(response, Project_id):
    username = models.User.objects.get(username=response.user)
    Project_obj = models.BBS_projects.objects.get(id=Project_id)
    comment_list = models.BBS_comments_projects.objects.filter(flag_id=Project_id)
    user_id = Project_obj.author_id
    author_obj1 = models.User.objects.get(id=user_id)
    author_obj = models.User_user.objects.get(user_id=user_id)
    Project_obj.view_count += 1
    Project_obj.save()
    return render(response, 'Project/item.html',
                  {'username': username, 'comment_list': comment_list, 'Project_obj': Project_obj,
                   'author_obj': author_obj, 'author_obj1': author_obj1})


def comment_sub(response):
    author = models.User.objects.get(username=response.user)
    models.BBS_comments_projects.objects.create(
        comment=response.POST.get('comment'),
        author=author,
        flag_id=response.POST.get('flag_id'),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        view_count=0,
    )
    flag_id = response.POST.get('flag_id')
    return HttpResponseRedirect(reverse('detail_pt', args=(flag_id,)))


def delete(request, project_id):
    project_obj = models.BBS_projects.objects.get(id=project_id)
    project_obj.delete()
    return HttpResponseRedirect("/Project/user_project/")


def project_sub(requset):
    author = models.User.objects.get(username=requset.user)
    models.BBS_projects.objects.create(
        title=requset.POST.get('title'),
        content=requset.POST.get('content'),
        tel=requset.POST.get('tel'),
        author=author,
        ranking=0,
        view_count=0,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    return HttpResponseRedirect("/Project/user_project/")


def user_project(response):
    username = models.User.objects.get(username=response.user)
    projectlist = models.BBS_projects.objects.filter(author=username)
    num_project = projectlist.count()
    return render(response, 'User/Project.html', {'username': username, 'projectlist': projectlist,
                                                  'num_project': num_project})
