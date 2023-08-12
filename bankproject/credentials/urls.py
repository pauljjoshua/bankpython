from . import views
from django.urls import path

urlpatterns = [


    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form',views.form,name='form'),
    path('app',views.app,name='app'),
    path('DROPDOWN',views.DROPDOWN,name='DROPDOWN'),
    path('fo',views.fo,name='fo'),

]