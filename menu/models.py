from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Виды меню'


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=255, verbose_name="Ссылка", blank=True, null=True)
    parent_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="Корневой пункт")
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE, verbose_name="Меню")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('parent_item__name', 'parent_item__parent_item__name')
        unique_together = ['name', 'parent_item']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
