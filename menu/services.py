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


def is_contain_url(child_items, url):
    result = False
    print("Child_items", child_items)
    print("URL:", url)
    if child_items is None:
        return result

    for key, value in child_items.items():
        print(key.url, url)
        if compare_urls(key.url, url):
            print("RETURN TRUE")
            return True

        result = is_contain_url(value, url)

    print("IS_Contain", result)
    return result

def compare_urls(url1, url2):
    url1 = set(url1.split('/'))
    url2 = set(url2.split('/'))

    return url1.issubset(url2)
