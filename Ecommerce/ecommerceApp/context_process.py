from .models import Category
from accountsApp.models import *

def categories(request):
    cat = Category.objects.all()
    resp = {'categories': cat}
    return resp

def login_checker(request):
    try:
        user_pic = Account.objects.get(user__id = request.user.id)
        user_pic = user_pic.profile_img
    except Exception as e:
        user_pic = ""
    return {"user_checker" : request.user.is_authenticated,
            "username" : request.user.username,
            "user_pic" : user_pic,
            }

