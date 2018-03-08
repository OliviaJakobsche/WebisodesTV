from django.http import HttpResponse

def index(request):
    return HttpResponse("Testowy widok homepage dla shows")