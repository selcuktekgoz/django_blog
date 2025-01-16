from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel


# from django.contrib.auth.models import User


class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to="yazi_resimleri")
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from="baslik", unique=True)
    kategoriler = models.ManyToManyField(
        KategoriModel, related_name="yazi"
    )  # ? ALAN EŞLEŞTİRİR bir yazının birden fazla kategoriye atılması için / kategoriye ait tüm  yazılara erişebilmek için releated / tabloda bunun adı bulunmaz panelde alanı bulunur. yeni tablo oluşturur iki tabloyu birleştirip
    yazar = models.ForeignKey(
        "account.CustomUserModel", related_name="yazilar", on_delete=models.CASCADE
    )  # ? bir tabloyu başka bir tabloyla ilişkilendirir / yazar üzerinden tğm yazılara erişmek / tabloya yazar_id atar

    class Meta:
        db_table = "yazi"
        verbose_name = "Yazı"
        verbose_name_plural = "Yazılar"

    def __str__(self):
        return self.baslik
