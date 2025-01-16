from django.db import models


class IletisimModel(models.Model):
    email = models.EmailField(max_length=255)
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = "iletisim"
        verbose_name = "İletişim"
        verbose_name_plural = "İletişim"

    def __str__(self):
        return self.email
