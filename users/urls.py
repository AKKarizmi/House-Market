from django.urls import path
from . import views

# USERS

urlpatterns = [
	path("login", views.login, name='login'),
	path("signup", views.signup, name='signup'),
	path("logout", views.logout, name='logout'),
	path("report", views.report, name='report'),
	# path("message", views.message, name='message'),
	# path("block", views.block, name='block'),
	path("update", views.update, name='update'),
	path("more", views.more, name='more')

]