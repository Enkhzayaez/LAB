from django.shortcuts import render, redirect
from .userForm import RegisterForm, AccountsForm
from django.contrib import auth, messages

def user_login(request):
    return render(request, 'accounts/signin.html')

def user_logout(request):
    pass

# def user_register(request):
#     if request.method == 'POST':
#         rform = RegisterForm(data=request.POST)
#         aform = AccountsForm(data=request.POST)
#         if rform.is_valid() and aform.is_valid():
#             user = rform.save()
#             user.set_password(user.password)
#             user.save()
#             acc = aform.save(commit=False)
#             acc.user = user
#             if 'profile_img' in request.FILES:
#                 acc.profile_img = request.FILES['profile_img']
#             acc.save()
#         else:
#             print(rform.errors, aform.errors)
#     else:
#         rform = RegisterForm()
#         aform = AccountsForm()
#         context = {
#             'rform': rform,
#             'aform': aform,
#         }
#     return render(request, 'accounts/register.html', context)

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
                messages.success(request, "registration is succesfull")
            else:
                messages.error(request, 'password not match')
        # return redirect('register')
    else:
        rform = RegisterForm()
        aform = AccountsForm()
        context = {
            'aform': aform,
            'rform': rform,
        }
        return render(request, 'accounts/register.html', context)
