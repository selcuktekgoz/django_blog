from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User


class YazilarModel(models.Model):
    resim = models.ImageField(upload_to="Yazi_resimleri")
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="baslik", unique=True)
    kategoriler = models.ManyToManyField(
        KategoriModel, related_name="yazi"
    )  # ? ALAN EŞLEŞTİRİR bir yazının birden fazla kategoriye atılması için / kategoriye ait tüm  yazılara erişebilmek için releated / tabloda bunun adı bulunmaz. yeni tablo oluşturur iki tabloyu birleştirip
    yazar = models.ForeignKey(
        User, related_name="yazilar", on_delete=models.CASCADE
    )  # ? bir tabloyu başka bir tabloyla ilişkilendirir / yazar üzerinden tğm yazılara erişmek / tabloya yazar_id atar

    class Meta:
        db_table = "yazi"
        verbose_name = "Yazı"
        verbose_name_plural = "Yazılar"
