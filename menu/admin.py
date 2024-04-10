from django.contrib import admin

from menu.models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'parent_item', 'menu']
    list_filter = ['parent_item']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name']

# class CustomOrderingMnuPointAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         return qs.order_by('my_custom_ordering')
