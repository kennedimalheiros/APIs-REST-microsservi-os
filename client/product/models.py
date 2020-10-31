from django.db import models


class Product(models.Model):
    barcode = models.PositiveIntegerField('Código de Barras', primary_key=True)
    name = models.CharField('Produto', max_length=100)

    def __str__(self):
        return f'({self.barcode}) - {self.name}'
