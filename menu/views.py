from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from menu.repositories import MenuItemRepository


def show_menu(request):
    return render(request, 'base.html', context={})


class GetParentItemsView(View):
    def get(self, request, *args, **kwargs):
        menu_id = self.kwargs.get('menu_id')
        parent_items = MenuItemRepository.get_parent_items(menu_id)
        return JsonResponse(list(parent_items), safe=False)
