# supermarket_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='inventory/', permanent=False)),  # 重定向到 inventory
    path('inventory/', include('inventory.urls')),
]