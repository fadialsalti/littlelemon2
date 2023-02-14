from django.contrib import admin 
from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
    path('api-token-auth/', obtain_auth_token),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]