from django.db import models


class DateAbstractModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now=False, auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
