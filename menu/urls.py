from django.urls import path, re_path

from menu import views

urlpatterns=[
    re_path(r'', views.show_menu),
]