from django import template
from menu.models import MenuItem
from menu.services import menu_to_dict

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu__name=menu_name)
    tree_menu_items = menu_to_dict(menu_items)
    print(f"TREE MENU: {tree_menu_items}")
    return {
        "menu_items": tree_menu_items,
        "active": 'block',
    }
