from django.shortcuts import render, redirect
from .forms import LoginForm
from register.models import Register

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = Register.objects.get(email=email)
            request.session['user_id'] = user.id
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})
