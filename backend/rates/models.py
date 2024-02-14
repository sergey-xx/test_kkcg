from django.db import models


class Rate(models.Model):
    cur_id = models.CharField('ID', max_length=10)
    num_code = models.IntegerField('NumCode')
    char_code = models.CharField('CharCode', max_length=3)
    name = models.CharField('Name', max_length=100)
    nominal = models.IntegerField('Nominal')
    value = models.DecimalField('Value', max_digits=7, decimal_places=4)
    previous = models.DecimalField('Previous', max_digits=7, decimal_places=4)

    def __str__(self) -> str:
        return self.char_code
