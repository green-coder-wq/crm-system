from django.db import models
from products.models import Product


class Advertisement(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название кампании")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Рекламируемая услуга")
    channel = models.CharField(max_length=255, verbose_name="Канал продвижения")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бюджет")

    class Meta:
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"

    def __str__(self):
        return self.name
