from datetime import datetime

from django.shortcuts import render
from django.db.models import Q

from chat.models import *



def simple_chat(request, userparameter=None):
    saye = Users.objects.filter(first_name="saye")[0]
    admin =  Users.objects.filter(first_name="admin")[0]
    amir= Users.objects.filter(first_name="amir")[0]
    yones= Users.objects.filter(first_name="yones")[0]
    parasto= Users.objects.filter(first_name="parasto")[0]
    farid= Users.objects.filter(first_name="farid")[0]
    homan= Users.objects.filter(first_name="homan")[0]
    
    if request.method == 'GET':
        
        users_len = 0
        convs = Conversations.objects.all()
        try:
            userparameter = '/'.join(e for e in userparameter if e.isalnum())
            selected_conv = Conversations.objects.filter(id=int(userparameter))[0]
            users = selected_conv.members.all()
            M = Messages.objects.filter(conversation_id=int(userparameter)).all()
        except :
            M = []
            users = []


    elif request.method == "POST":
        userparameter = '/'.join(e for e in userparameter if e.isalnum())
        c = Conversations.objects.filter(id=int(userparameter))[0]
        users = c.members.all()
        users_len = len(users)
        Messages(sender_id = admin,
                conversation_id =c,
                text =request.POST['text'],
                date = datetime.now(),
                ).save()
        M = Messages.objects.filter(
            conversation_id=int(userparameter)
        )
        convs = Conversations.objects.all()
    
    return render(
        request,
        'chatroom.html',
        {   "users":users,
            "saye": saye,
            "homan":homan,
            "farid":farid,
            "amir":amir,
            "yones":yones,
            "parasto":parasto,
            "admin" : admin,
            "messages": M,
            "conversations": convs,
            "users_len":users_len,
        }
    )




def inboxes(request):
    users_list = Users.objects.all()
    for u in users_list:
        u.recieved_messages = 0
        for c in u.conversations_set.all():
            u.recieved_messages += len(Messages.objects.filter(Q(conversation_id = c)).filter(~Q(sender_id=u)))

    return render(
                  request,
                  "inboxes.html",{
                    "users_list":users_list,
                    
                  }
                  )


