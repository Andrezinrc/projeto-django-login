from django.shortcuts import render, redirect
from register.models import Register
from .forms import LoginForm
from django.contrib import messages
import time

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = Register.objects.get(email=email)
            request.session['user_id'] = user.id

            messages.success(request, 'Login feito co sucesso.')
            time.sleep(3)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})
