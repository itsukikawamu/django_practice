from django.http import HttpResponse

def test(request):
    return HttpResponse("test: Can you see this massage?")