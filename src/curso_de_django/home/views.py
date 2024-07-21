from django.shortcuts import render

def home(request):
    mensage = "Hello, World"
    description = "Estou aprendendo Django!"
    logo = "<Dev360/>"

    context = {
        'mensage': mensage,
        'description': description,
        'logo': logo,
    }
    return render(request, 'home/home.html', context)
