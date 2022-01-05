from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('postsignIn/', views.postsignIn),
    path('profile/', views.profile,name='profile'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('postsignUp/', views.postsignUp),
    path('logout/', views.logout, name="log"),
    path('reset/', views.reset, name="reset"),
    path('postReset/', views.postReset),
    path('create/',views.create,name='create'),
]