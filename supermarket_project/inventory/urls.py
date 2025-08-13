# inventory/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 主页
    path('add/', views.add_product, name='add_product'),  # 添加产品页面
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # 删除产品页面
]