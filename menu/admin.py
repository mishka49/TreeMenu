from django.contrib import admin

from menu.models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'parent_item', 'menu']
    list_filter = ['parent_item', 'menu__name']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent_item":
            print(kwargs.items())
            kwargs["queryset"] = MenuItem.objects.filter(menu__name="Основное")

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name']
