from .models import Category

def categories(request):
    cat = Category.objects.all()
    resp = {'categories': cat}
    return resp


