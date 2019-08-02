from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello there")



class User:
    
    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
        # return self.first_name + ' ' + self.last_name

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)



def search_query(query):
    result = []
    for u in users:
        if u.first_name == query:
            result.append(u)
    return result

users = [
    User('Vahid', 'Kharazi', [1, 2, 18]),
    User('Sara', 'Ahmadi', [4, 20, 15]),
    User('Tarane', 'Ali Doosti', [17, 7])
]

def user_list(request):
    Q = request.GET['search']
    result = (search_query(Q))
    return render(
        request,
        'userlist.html',
        {
            "users": result,
            
        }
    )