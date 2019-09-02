from django.conf.urls import url
from safetraveller import views
urlpatterns = [
	url(r'^$',views.main,name='main'),
	url(r'^login/$',views.user_login, name='login'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^register/$',views.register, name='register'),
	#add any question number here in url


]