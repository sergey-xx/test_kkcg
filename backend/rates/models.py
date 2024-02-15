from django.db import models


class Rate(models.Model):
    charcode = models.CharField('CharCode',
                                max_length=3,
                                null=False,
                                blank=False)
    rate = models.DecimalField('Rate',
                               max_digits=7,
                               decimal_places=4,
                               null=False,
                               blank=False)
    date = models.DateField("Date",
                            auto_now=False,
                            auto_now_add=False,
                            null=False,
                            blank=False)

    def __str__(self) -> str:
        return self.charcode
