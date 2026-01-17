from django.urls import path, include
from . import views

urlpatterns = [
    path('user/register',views.RegisterUserAPiVIew.as_view()),
    path('user/login', views.LoginUserAPIView.as_view()),
    path('user/logout', views.LogoutAPIview.as_view()),
    path('user/deleto/<int:pk>', views.UserDelete.as_view()),

    path('profile/', views.ProfileCreateList.as_view()),
    path('profile/<int:pk>', views.ProfileUDD.as_view()),
]

