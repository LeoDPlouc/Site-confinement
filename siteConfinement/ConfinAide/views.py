from django.http import HttpResponse


def index(request):
    return HttpResponse("Alors, on a le covid?")