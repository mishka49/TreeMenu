from django.urls import path, re_path

from menu import views
from menu.views import GetParentItemsView

urlpatterns = [
    path('get_parent_items/<int:menu_id>/', GetParentItemsView.as_view(), name='get_parent_items'),
    re_path(r'', views.show_menu),
]
