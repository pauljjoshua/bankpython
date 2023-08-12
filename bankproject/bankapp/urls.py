from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    # path('login/',views.login,name='login'),
    # path('register/',views.register,name='register'),
    # # path('logout/',views.logout,name='logout'),
    # # path('branches',views.branches,name='branches'),
    # path('contact/',views.contact,name='contact'),

]