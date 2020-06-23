from django.urls import path
from .import views

urlpatterns = [
    path('', views.login,name='loginpage'),
    #path('Gallery',views.login,name='photo'),
    path('logout',views.logout,name='logout'),
    path('indexx',views.indexx,name='indexx'),
    path('photos.html', views.photos, name='photo'),
    path('bio.html',views.bio,name='photo'),
    path('blog.html', views.blog, name='photo'),
    path('contact.html', views.contact, name='photo'),
    path('index.html', views.indexx, name='photo'),
    path('single.html',views.single,name='single'),
    path('signup.html',views.signup,name='signup'),
    path('login', views.login,name='loginpage'),
    path('signup',views.signup,name='signup'),

]
