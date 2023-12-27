from django.http import HttpResponse

def say_hello(request):
    message = 'Hello World!'
    
    return HttpResponse(message, content_type='text/plain')