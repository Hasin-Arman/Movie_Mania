from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('signin/',views.SignInView.as_view(),name="signin"),
    path('signout/',views.SignOutView.as_view(),name="signout"),
    path('password/',views.change_password.as_view(),name="password"),
    path('update/<int:pk>/',views.update_profile.as_view(),name="update"),
]
