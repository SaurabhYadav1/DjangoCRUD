from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout


def sign_up_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    template_name = 'auth_app/sign_up.html'
    context = {'form': form}
    return render(request,template_name,context)

def signin_view(request):
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('show_url')
    template_name = 'auth_app/signin.html'
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('signup_url')