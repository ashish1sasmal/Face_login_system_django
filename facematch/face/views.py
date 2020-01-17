from django.shortcuts import render
from .forms import *
from base64 import b64encode
from face_recognition import load_image_file,face_encodings,compare_faces

# Create your views here.

def home(request):
	if request.method=='POST':
		form=MatchForm(request.POST, request.FILES)
		if form.is_valid():
			# form.save()

			img1=form.cleaned_data['img1']
			img2=form.cleaned_data['img2']
			
			
			img1=load_image_file(img1)
			enc1=face_encodings(img1)[0]

			img2=load_image_file(img2)
			enc2=face_encodings(img2)[0]
			res=compare_faces([enc1],enc2)

			return render(request, 'result.html',{'result':res[0],'img1':inp1,'img2':inp2})
	else:
		form=MatchForm()

	return render(request, 'home.html',{'form':form})
