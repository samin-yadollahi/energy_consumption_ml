from django.urls import path
from django.contrib import admin
from rest_framework import routers


routers = routers.DefaultRouter()

urlpatterns = routers.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]