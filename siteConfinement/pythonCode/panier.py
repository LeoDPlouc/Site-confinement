from django.http import HttpRequest

def Update(request):
    p = request.POST["p"]
    n = request.POST["n"]

    request.session[p] = int(request.session[p]) + n