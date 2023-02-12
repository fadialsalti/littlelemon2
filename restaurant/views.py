from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .models import Menu, Booking
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (AllowPostAnyReadAuthenticatedUser,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return User.objects.all()
    #     return User.objects.filter(username=user.username)