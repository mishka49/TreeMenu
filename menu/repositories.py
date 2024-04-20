from menu.models import MenuItem


class MenuItemRepository:
    @staticmethod
    def get_parent_items(menu_id: int):
        return MenuItem.objects.filter(menu__id=menu_id).values('id', 'name')

    @staticmethod
    def get_menu_items(menu_name: str):
        return MenuItem.objects.filter(menu__name=menu_name)
