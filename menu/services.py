from menu.models import MenuItem


def menu_to_dict(menu_items: MenuItem, parent_item=None):
    items = dict()
    segment_menu = menu_items.filter(parent_item=parent_item)

    if len(segment_menu) == 0:
        return None

    for item in segment_menu:
        result = menu_to_dict(menu_items, item)
        items[item] = result

    return items
