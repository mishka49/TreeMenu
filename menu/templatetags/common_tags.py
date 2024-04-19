from django import template
from menu.models import MenuItem
from menu.services import menu_to_dict, is_contain_url, compare_urls

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name, request):
    menu_items = MenuItem.objects.filter(menu__name=menu_name)
    tree_menu_items = menu_to_dict(menu_items)
    print(f"TREE MENU: {tree_menu_items}")
    return {
        "menu_items": tree_menu_items,
        "active": 'block',
        "request": request,
    }


@register.simple_tag
def is_contain_active_item(item, url):
    result = is_contain_url(item, url)
    return result

@register.simple_tag
def is_urls_same(url1, url2):
    return compare_urls(url1,url2)