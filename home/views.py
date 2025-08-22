from django.shortcuts import render, redirect
from home.models import House, Data
from django.contrib import messages
import random
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
# from .utitles import find_max
# Create your views here.

def login(request):
	return render(request, 'login.html')

def index(request):
	homes = House.objects.all()
	return render(request, 'index.html', {'home': homes,})

def upload(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['file']
		location = request.POST['location']
		price = request.POST['price']
		phone = request.POST['phone']
		room = request.POST['room']
		floor = request.POST['floor']
		owner = request.POST['owner']
		fs = FileSystemStorage()
		image = fs.save(uploaded_file.name, uploaded_file)

		other = House.objects.create(image=image ,location=location, price=price, phone=phone, rooms=room, floors=floor, owner=owner)
		other.save()
		return redirect("/index")

def search(request):
	homes = House.objects.all()
	if request.method == 'GET':
		location = request.GET['location']
		rooms = request.GET['rooms']
		price = request.GET['price']

		find = House.objects.filter(location=location, rooms=rooms, price=price)

		if find:
			return render(request, 'Result.html', {'find': find, 'home': homes})		
		else:
			messages.error(request, 'No Result Found')
			return redirect("/index")
	else:
		return redirect("/")

def show_all(request):
	if request.method == 'GET':
		input_index = request.GET['input']
		output = House.objects.filter(id=input_index)
		return render(request, 'shower.html', {'filter': output})

def delete(request):
	if request.method == 'GET':
		delete = request.GET['delete']
		delete_1 = House.objects.filter(id=delete)
		delete_1.delete()
		return redirect('/index')

def my_page(request):
	# if request.method == 'GET':
	# 	data = request.GET['data']
	# 	data_1 = request.GET['data_1']
	# 	data_2 = request.GET['data_2']
	# 	data_3 = request.GET['data_3']
	# 	user_id = request.GET['user_id']
	# 	filter_data = House.objects.filter(location=data)
	# 	filter_data_1 = House.objects.filter(location=data_1)
	# 	filter_data_2 = House.objects.filter(location=data_2)
	# 	filter_data_3 = House.objects.filter(location=data_3)
	# 	filter_result = Data.objects.create(price=filter_data.price, image=filter_data.image)
	# 	filter_result.save()
		return redirect("/index")


		
