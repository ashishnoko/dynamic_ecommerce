from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'pages/home/home.html')


def contact(request):
    content = {
        'title': "Contact Us"
    }
    return render(request, 'pages/contact/contact.html',content)
