from django.contrib.auth.views import LoginView
from django.urls import path


from .views import (MyLogoutView,
                    RegisterView,
                    )


app_name = 'account'
urlpatterns = [
    path('login/',
         LoginView.as_view(
             template_name='account/login.html',
             redirect_authenticated_user=True
         ), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]