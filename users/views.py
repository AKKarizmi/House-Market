from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Photo
from users.models import me
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
# Create your views here.


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/index')
		else:
			messages.error(request, 'رمز کاربری و یا نام کاربری درست نمی باشد')
			return redirect("/")		

def logout(request):
	auth.logout(request)
	return redirect("/")

def signup(request):
	if request.method == 'POST':
		first_name = request.POST['firstname']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['pass']
		re_pass = request.POST['repeat-pass']
		if password == re_pass:
			user = User.objects.create_user(username=username, password=re_pass, email=email, first_name=first_name)
			user.save()
			return redirect("/")
		else:
			return redirect('map/register')

def report(request):
	if request.method == 'POST':
		input_user = request.POST['report']
		user_found = User.objects.filter(id=input_user)
		t_user = Photo.objects.all()
		return render(request, "user/more.html", {'user': user_found, 'detail': t_user})

def update(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['file']
		jet = request.POST['jet']
		saved = fs.save(uploaded_file.name, uploaded_file)
		done = Photo.objects.create(mental=saved, money=jet)
		done.save()
		return redirect('/map/profile')		

def more(request):
	if request.method == 'POST':
		last_name = request.POST['last_name']
		live = request.POST['live']
		main = request.POST['main']
		about = request.POST['about']
		button = request.POST['button']
		add = User.objects.create(last_name=last_name)
		add_1 = me.objects.create(live=live, main=main, about=about, name=button)
		add.save()
		add_1.save()
		return redirect("/map/profile")


