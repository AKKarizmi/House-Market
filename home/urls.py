from django.urls import path
from . import views
urlpatterns = [
	path("", views.login, name='login'),
	path("index", views.index, name='index'),
	path("upload", views.upload, name='upload'),
	path("search", views.search, name='search'),
	path("show_all", views.show_all, name='show_all'),
	path("delete", views.delete, name='delete'),
	path("my_page", views.my_page, name='my_page')


]