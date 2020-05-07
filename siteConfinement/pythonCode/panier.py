from django.http import HttpRequest

def Update(request):
    p = request.POST["p"]
    n = request.POST["n"]
