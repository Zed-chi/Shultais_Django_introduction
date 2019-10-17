from django.db import models


class House(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    price = models.IntegerField(verbose_name="цена")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(
        verbose_name="фото", upload_to="houses/photos", default="", blank=True
    )

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        ordering = ["name"]

    def __str__(self):
        return self.name
