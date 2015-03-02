from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from audiofield.forms import CustomerAudioFileForm
#from django.template.context_processors import csrf
from django.core.context_processors import csrf
import os
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def add_audio(request):
	template = 'audio.html'
	form = CustomerAudioFileForm()

	# Add audio
	if request.method == 'POST':
		form = CustomerAudioFileForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = User.objects.get(username=request.user)
			obj.save()
			return HttpResponseRedirect('/')

		# To retain frontend widget, if form.is_valid() == False
		#form.fields['audio_file'].widget = CustomerAudioFileWidget()

	data = {
		'audio_form': form,
	}

	c = {}
	c.update(csrf(request))	

	return render_to_response(template, data,
		   context_instance=RequestContext(request, c))


    

