from django.urls import path
from .views import Login, logout_views


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_views, name='logout'),
]