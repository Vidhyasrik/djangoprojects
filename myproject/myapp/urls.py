from django.urls import path

from .views import Home

urlpatterns = [
        path('user/', Home.as_view(), name='home'),
]