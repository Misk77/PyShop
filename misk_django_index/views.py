from django.http import HttpResponse


# Create your views here.
def misk_django_index(request):
    return HttpResponse('Hello World\nMichel skoglund django page INDEX: misk_django_index')


def misk_django_aboutMe(request):
    return HttpResponse('Om michel skoglund: misk_django_aboutMe ')
