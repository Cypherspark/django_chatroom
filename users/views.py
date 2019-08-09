from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from chat.models import Users 

def user_list(request):
    if request.method == 'GET':
        try:
            print(request.GET)
            query = request.GET['search']

            users = Users.objects.filter(first_name__startswith=query)
        except MultiValueDictKeyError:
            users = Users.objects.all()

        return render(
            request,
            'userlist.html',
            {
                "users": users,
            }
        )

    elif request.method == "POST":
        Users(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            number_of_friends=132
        ).save()
        users = Users.objects.all()
        return render(
            request,
            'userlist.html',
            {
                "users": users,
            }
        )