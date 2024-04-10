from django.db import models


class MenuPoint(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=255, verbose_name="Ссылка")
    parent_point = models.ForeignKey('MenuPoint', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
