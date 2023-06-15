from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('', include('Charlist.urls'))
    

]
