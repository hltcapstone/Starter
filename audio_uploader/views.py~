from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from audiofield.forms import CustomerAudioFileForm
#from django.template.context_processors import csrf
from django.core.context_processors import csrf
import os


# Create your views here.

#@login_required
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
            return HttpResponseRedirect('/audio')

        # To retain frontend widget, if form.is_valid() == False
        form.fields['audio_file'].widget = CustomerAudioFileWidget()

    data = {
       'audio_form': form,
    }
    #c = RequestContext(request.POST, {})
    '''c = {}
    c.update(csrf(request))'''

    #return render_to_response(template, data:c[data], RequestContext(request, {}))
    return render_to_response(template, data, context_instance=RequestContext(request))
    #return render_to_response(template, c)

def upload_audio(request):
	state = 'Upload Audio'
	if (request.GET.get('data')):
		os.system("mv" + data + " /home/hlt/Desktop/Test")
		if (request.GET.get('upload')):
			os.system("tsunamid *")
			state = 'Audio Successfully Uploaded!'
		
	return render_to_response('auth.html', {state:'state'})

'''from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadAudioForm

def upload_file(request):
	if request.method == 'POST':
		form = UploadAudioForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/login.html')
	else:
		form = UploadAudioForm()
	return render_to_response('audio.html', {'form': form})'''
    

