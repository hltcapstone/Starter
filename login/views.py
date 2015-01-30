from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
#from django.core.context_processors import csrf

# Create your views here.

# login/views.py
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    c = {}
    c.update(csrf(request))

    #return render_to_response('audio.html',{'state':state, 'username': username}, RequestContext(response, c))
    #return render_to_response(('audio.html',c), RequestContext(request))
    return render('audio.html',{'state':state, 'username': username}, RequestContext(response, c))