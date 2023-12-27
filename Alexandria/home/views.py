from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def sample(request):
    data = {
        'books': [
            {'title': 'Frankenstein',
             'author': 'Shelley, Mary'
             },
            {
                'title': 'Metamorphosis',
                'author': 'Kafka, Franz',
                'recommended': True
            },
            {
                'title': 'Dracula',
                'author': 'Stocker, Bram',
                'recommended': False
            }
        ]
    }

    return render(request, "sample.html", data)


def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")