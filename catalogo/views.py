from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("¡Bienvenido a la página de inicio del catálogo!")
