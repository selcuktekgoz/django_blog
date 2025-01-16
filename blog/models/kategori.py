from django.db import models
from autoslug import AutoSlugField


class KategoriModel(models.Model):
    isim = models.CharField(
        verbose_name="Kategori Adı", max_length=50, blank=False, null=False
    )
    slug = AutoSlugField(populate_from="isim", unique=True)

    class Meta:
        db_table = "kategori"
        verbose_name_plural = "Kategoriler"
        verbose_name = "Kategori"

    def __str__(self):
        return self.isim
