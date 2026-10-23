from django.db import models
from products.models import Product


class Contract(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Услуга")
    document = models.FileField(upload_to='contracts/', verbose_name="Документ")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"

    def __str__(self):
        return self.name
