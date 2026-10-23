from django.db import models
from advertisements.models import Advertisement


class Lead(models.Model):
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    advertisement = models.ForeignKey(
        Advertisement, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Рекламная кампания"
    )

    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
