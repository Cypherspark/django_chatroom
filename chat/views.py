from datetime import datetime

from django.shortcuts import render

from chat.models import *



def simple_chat(request, userparameter):
    saye = Users.objects.filter(first_name="saye")[0]
    admin =  Users.objects.filter(first_name="admin")[0]
    amir= Users.objects.filter(first_name="amir")[0]
    yones= Users.objects.filter(first_name="yones")[0]
    parasto= Users.objects.filter(first_name="parasto")[0]
    farid= Users.objects.filter(first_name="farid")[0]
    homan= Users.objects.filter(first_name="homan")[0]
    if request.method == 'GET':
        print('salam')
        convs = Conversations.objects.all()
        try:
        
            selected_conv = Conversations.objects.filter(id=int(userparameter))[0]
            users = selected_conv.members.all()
            M = Messages.objects.filter(conversation_id=int(userparameter)).all()
        except ValueError:
            M = []
            users = []

        return render(
                    request,
                    'chatroom.html',
                    {
                        "saye": saye,
                        "homan":homan,
                        "farid":farid,
                        "amir":amir,
                        "yones":yones,
                        "parasto":parasto,
                        "users" : users,
                        "messages": M,
                        "conversations": convs,
                        "admin" : admin,
                    }
                    )


    elif request.method == "POST":
        
        c = Conversations.objects.filter(id=int(userparameter))[0]
        users = c.members.all()
        Messages(sender_id = admin,
                conversation_id =c,
                text =request.POST['text'],
                date = datetime.now(),
                ).save()
        M = Messages.objects.filter(
            conversation_id=int(userparameter)
        )
        # except ValueError:
        #     print("there is no userparameters")
        #     M = []

        
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
            }
        )






