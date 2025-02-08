from django.http import HttpResponse

def youtube(request):
    return HttpResponse("<h1>hello, this is YouTube.</h1><p>welcome!</p>")