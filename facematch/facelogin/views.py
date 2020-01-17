from django.shortcuts import render,redirect
from .forms import UserForm,ProfileForm,SnapForm
from django.contrib.auth import authenticate

from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
import os
from .models import Snaps
import face_recognition
from django.views.generic import TemplateView
from django.http import HttpResponse

import cgi
from base64 import b64decode



def home(request):
    return render(request,'index.html')

@login_required
def user_logout(request):
	logout(request)
	return redirect('home')

# def facelogin(loc):
# 		# url = "Some url to stream"
# 		# video = pafy.new(url)
# 		# best = video.getbest(preftype="webm")
# 		img1=loc
# 		video_capture = cv2.VideoCapture(0)
#
		# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		# MEDIA_ROOT =os.path.join(BASE_DIR)
		# loc=(str(MEDIA_ROOT)+loc)
# 		# # Load a sample picture and learn how to recognize it.
# 		# img1 = face_recognition.load_image_file(loc)
# 		enc1= face_recognition.face_encodings(img1)[0]
# 		process_this_frame = True
# 		while True:
# 			# Grab a single frame of video
# 			ret, frame = video_capture.read()
# 			if ret:
# 			# Resize frame of video to 1/4 size for faster face recognition processing
# 				small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#
# 				# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
# 				rgb_small_frame = small_frame[:, :, ::-1]
#
# 				# Only process every other frame of video to save time
# 				if process_this_frame:
# 					# Find all the faces and face encodings in the current frame of video
# 					face_locations = face_recognition.face_locations(rgb_small_frame)
# 					face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#
# 					face_names = []
# 					for face_encoding in face_encodings:
# 						print("y")
# 						# See if the face is a match for the known face(s)
# 						matches = face_recognition.compare_faces([enc1], face_encoding)
# 						name = "Unknown"
# 						if True in matches:
# 							print("SUccess")
# 							video_capture.release()
# 							cv2.destroyAllWindows()
# 							return True
# 						else:
# 							print("unsuccess")
# 							video_capture.release()
# 							cv2.destroyAllWindows()
# 							return False
#
# 				process_this_frame = not process_this_frame
# 			else:
# 				print("false")
# 				return false


# Release handle to the webcam




def register(request):
	print('register .....')

	if request.method=="POST":
		print("recieving...")
		userform=UserForm(data=request.POST)
		profileform=ProfileForm(request.POST,request.FILES)
		print(userform.errors)
		print(profileform.errors)
		if userform.is_valid() and profileform.is_valid():

			user=userform.save(commit=False)
			user.username=userform.cleaned_data.get('email')
			user.save()
			print('user save')
			profile=profileform.save(commit=False)
			profile.user=user
			if 'image' in request.FILES:
				profile.image=request.FILES['image']
				profile.save()
				print('success')
				messages.success(request, 'Your account has been created !')
				return redirect('home')
		else:
			print('error')
	else:
		userform=UserForm()
		profileform=ProfileForm()

	return render(request, 'register.html',{'form':userform,'profile':profileform})





def user_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=authenticate(username=email,password=password)
        if user:
            loc=user.profile.image.url
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            MEDIA_ROOT =os.path.join(BASE_DIR)
            loc=(str(MEDIA_ROOT)+loc)
            print(loc)
            data=request.POST.get('current_image')
            data_uri = data
            header, encoded = data_uri.split(",", 1)
            data = b64decode(encoded)
            with open("media/login/"+str(user.username)+".png", "wb") as f:
                f.write(data)

            # form=Snaps(user=user,image="media/login/"+str(user.username)+".png")
            # form.save()
            got_image = face_recognition.load_image_file("media/login/"+str(user.username)+".png")

            existing_image = face_recognition.load_image_file(str(loc))
            existing_image_facialfeatures = face_recognition.face_encodings(existing_image)[0]
            print("y")
            got_image_facialfeatures = face_recognition.face_encodings(got_image)
            if got_image_facialfeatures!=[]:
                print(got_image_facialfeatures)
                got_image_facialfeatures=got_image_facialfeatures[0]
                results= face_recognition.compare_faces([existing_image_facialfeatures],got_image_facialfeatures)

                if results[0]:
                    login(request,user)
                    messages.success(request, 'Congratulations! You have been Successfully Logged IN using face recognition !')
                    return redirect('home')

                else:
                    messages.warning(request,'Sorry ! Face does not match')
                    return redirect('login')
            else:
                messages.warning(request,'Can\'t capture Bright image of face !')
                return redirect('login')
    return render(request, 'tree.html')
