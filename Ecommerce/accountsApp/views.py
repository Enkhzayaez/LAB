from django.shortcuts import render, redirect
from .userForm import RegisterForm, AccountsForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            messages.success(request, message='success')
            auth.login(request, user)
            return redirect('/')

    return render(request, 'accounts/signin.html')

@login_required(login_url="login")
def user_logout(request):
    if request.method == "GET":
        auth.logout(request=request)
    return redirect('/')

def user_register(request):
    if request.method == "POST":
        rform = RegisterForm(data=request.POST)
        aform = AccountsForm(data=request.POST)
        if rform.is_valid() and aform.is_valid():
            if rform['password'].value() == rform['repeat_password'].value():
                rform.instance.username = str(rform['email'].value()).split(sep="@")[0]
                user = rform.save()
                user.set_password(user.password)
                user.save()

                acc = aform.save(commit=False)
                acc.user = user
                if 'profile_img' in request.FILES:
                    acc.profile_img = request.FILES['profile_img']
                acc.save()
                messages.success(request,"registration is succesfull")
            else:
                messages.error(request, 'password not match')
        return redirect('login')
    else:
        rform = RegisterForm()
        aform = AccountsForm()
        context = {
            'aform': aform,
            'rform': rform,
        }
        return render(request, 'accounts/register.html', context)
