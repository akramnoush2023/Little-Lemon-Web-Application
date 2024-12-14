from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('', views.homepage),
    path('menus/', views.menus, name='menus'),
    path('users/', views.UserView.as_view())
]