from django import template

from menu.models import MenuItem
from menu.repositories import MenuItemRepository
from menu.services import menu_to_dict, is_contain_url, compare_urls

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name: str, request):
    menu_items = MenuItemRepository.get_menu_items(menu_name)
    tree_menu_items = menu_to_dict(menu_items)
    return {
        "menu_items": tree_menu_items,
        "active": 'block',
        "request": request,
    }


@register.simple_tag
def is_contain_active_item(item: dict, url: str):
    result = is_contain_url(item, url)
    return result


@register.simple_tag
def is_urls_same(url1: str, url2: str):
    return compare_urls(url1, url2)
