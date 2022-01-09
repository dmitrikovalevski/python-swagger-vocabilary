from django.http import HttpResponse
from django.shortcuts import render
from .models import Card


def index(request):
    return HttpResponse(""
                        "<div><center>"
                        "<h2>Hello vocabilary</h2>"
                        "<button><a href=\"admin/\">ADMIN</a></button>"
                        "<button><a href=\"all_models/\">CARDS</a></button>"
                        "<button><a href=\"swagger/\">SWAGGER</a></button>"
                        "</div></center>"
                        "")


def all_models(request):
    all_cards = Card.objects.all()
    context = {
        'cards': all_cards
    }
    return render(request, 'index.html', context)
