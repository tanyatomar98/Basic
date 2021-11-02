from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import UserName
from .forms import SigninForm, SignInForm2

# Create your views here.

def user_profile_view(request):
    user1 = UserName.objects.get(id=2)
    context = {
        'object' : user1
    }
    return render(request, "profile/user_profile.html", context)

# Method 2 Sign in view
# In this method we are saving forms using create method 
# And we are many checking by ourself 

# def sign_in_view(request):
      # creating an empty sign in form initially for initial get method
#     my_form = SignInForm2()

#     if request.method == 'POST':
#         my_form = SignInForm2(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             UserName.objects.create(**my_form.cleaned_data)
            
#         else:
#             print(my_form.errors)
#         #Clearing form after saving data
#         my_form = SignInForm2()

#     #Dictionary help in passing form elements to html page
#     context = {
#         'form' : my_form
#     }
#     return render(request, "profile/signin.html", context)


# Method 1 sign in view
# Form get save using .save method
# Easy method because validation get done at once
def sign_in_view(request):
    initial_data = {
        'name'   : '<username>geek',
        'email'  : '<username>@geek.edu'
    }
    # request.POST is used for post method
    # Else render Empty form so None is used
    # obj = UserName.objects.get(id=1)
    # print(UserName.objects.get(id=1))
    form = SigninForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        # clearing form after submitting
        form = SigninForm()
    context = {
        # Assigning form object to avoid assigning each form object element 
        'form' : form
    }
    return render(request, "profile/signin.html", context)

# def sign_in_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#     print(name)
#     return render(request, "profile/signin.html", {})

# Dynamic view
def dynamic_view(request, my_id):
    # obj = UserName.objects.get(id=my_id)
    obj = get_object_or_404(UserName, id=my_id)
    context = {
        'object' : obj
    }
    return render(request, 'profile/dynamic.html', context)

def user_delete_view(request, my_id):
    obj = get_object_or_404(UserName, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object' : obj
    }
    return render(request, 'profile/delete_user.html', context)

# Objects list
def Users_list_view(request):
    queryset = UserName.objects.all()
    context = {
        'users_list' : queryset
    }
    return render(request, 'profile/users.html', context)