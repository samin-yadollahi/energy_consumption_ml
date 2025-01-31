from django.urls import path
from django.contrib import admin
from ec_api import views as ec_api_views
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('ec_prediction/', ec_api_views.InputDataAPIView.as_view()),
]