from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from workspace.views import index


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(index)
            else:
                return render(request, 'login.html', {'form': form,
                                                      'error': 'The following account has not been activated'})
        else:
            return render(request, 'login.html', {'form': form,
                                                  'error': 'Username or password are incorrect'})
    return render(request, 'login.html', {'form': form})
