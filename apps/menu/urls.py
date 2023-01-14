from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeMenu.as_view(), name="home"),
    path('sub_menu/<str:name>', views.SubMenu.as_view(), name='sub_menu'),
    path('detail_menu/<str:name>', views.DetailMenu.as_view(), name='detail_menu')
]