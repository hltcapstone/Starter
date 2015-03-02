from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext

# Create your views here.

# login/views.py
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login


def login_user(request):
	state = "Please log in below..."
	check = False
	username = password = ''
	c = {}
	c.update(csrf(request))
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		#username = request.POST['username']
		#password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're successfully logged in!"
				check = True
				return render_to_response('audio.html',{'state':state, 'username': username}, RequestContext(request, c))
			else:
				state = "Your account is not active, please contact the site admin."
				return render_to_response('auth.html',{'state':state, 'username': username}, RequestContext(request, c))
		else:
			state = "Your username and/or password were incorrect."
			return render_to_response('auth.html',{'state':state, 'username': username}, RequestContext(request, c))

	return render_to_response('auth.html',{'state':state, 'username': username}, RequestContext(request, c))
    

    
    #return render_to_response(('audio.html',c), RequestContext(request))
    #return render('audio.html',{'state':state, 'username':username}, RequestContext(response, c))

#def loginUser(request):
#	c = RequestContext(request.POST, {})
#	#c.update(csrf(request))
#	username = request.POST['username']
#	password = request.POST['password']
#	user = authenticate(username=username, password=password)
#	if user is not  None:
#		if user.is_active:
#			login(request, user)
#		else:
#			print 'Disabled account'
#	else:
#		print 'invalid username or password'
	#return render_to_response('audio.html', RequestContext(response, {}))
#	return render_to_response('audio.html', c)
