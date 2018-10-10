from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, RegistrationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
# Create your views here.

@login_required(login_url="login/")
def profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,"profile.html", args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = user.refresh_from_db()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # args = {'user': form.cleaned_data}
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return redirect('/register')
            # return render(request, 'profile.html', context_instance=RequestContext(request))
            
            # return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'sign_up.html', args)