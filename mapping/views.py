from django.shortcuts import render
from home.models import House
from home.models import Photo
from users.models import me
from django.contrib.auth.models import User, auth
# Create your views here.

# MAPPING

def list(request):
	home = House.objects.all()
	return render(request, 'list.html', {'home': home})

def upload(request):
	return render(request, 'Upload.html')	

def register(request):
	return render(request, 'register.html')	

def edit(request):
	data_choice = House.objects.all()
	return render(request, 'edit.html', {'data': data_choice})

def report(request):
	return render(request, 'Report.html')

def profile(request):
	done = Photo.objects.all()
	more = me.objects.all()
	return render(request, 'Profile.html', {'detail': done, 'INFO': more})	

def update(request):
	if request.method == 'POST':
		btn = request.POST['btn']		
		return render(request, 'user/update.html', {'update': btn})
	else:
		return render(request, 'user/update.html')	

def user_detail(request):
	all_user = User.objects.all()
	t_user = Photo.objects.all()
	return render(request, 'user/details.html', {'user': all_user, 'detail': t_user})

	