
from django.urls import path
from Userauths import views

app_name = 'Userauths'
urlpatterns = [
    path('',views.register_view, name='signup'),
    path('login/',views.login_view, name='signin'),
    path('logout/',views.logout_view, name='signout')
]
