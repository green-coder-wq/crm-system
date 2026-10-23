from django.db import models
from leads.models import Lead
from contracts.models import Contract


class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, verbose_name="Потенциальный клиент")
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, verbose_name="Контракт")

    class Meta:
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"

    def __str__(self):
        return f"{self.lead.last_name} {self.lead.first_name}"
