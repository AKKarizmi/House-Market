from django.urls import path
from . import views
# MAPPING
urlpatterns = [
	path("list", views.list, name='list'),
	path("upload", views.upload, name='upload'),
	path("register", views.register, name='register'),
	path("edit", views.edit, name='edit'),
	path("report", views.report, name='report'),
	path("profile", views.profile, name='profile'),
	path("update", views.update ,name='update'),
	path("user_detail", views.user_detail, name='user_detail'),
	

]