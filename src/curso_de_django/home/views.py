from django.shortcuts import render

def home(request):
    mensage = "Hello, World"
    description = "Estou aprendendo Django!"

    context = {
        'mensage': mensage,
        'description': description,
    }
    return render(request, 'home/home.html', context)
