from django.db import models
from houses.models import House

# Create your models here.
class Order(models.Model):
    house = models.ForeignKey(
        House, verbose_name="дом", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, verbose_name="имя клиента")
    phone = models.CharField(max_length=255, verbose_name="телефон")
    date = models.DateTimeField(verbose_name="дата", auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
