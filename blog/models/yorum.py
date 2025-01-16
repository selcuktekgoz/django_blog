from django.db import models
from blog.models import YazilarModel
from blog.abstract_models import DateAbstractModel

# from django.contrib.auth.models import User


class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey(
        "account.CustomUserModel", on_delete=models.CASCADE, related_name="yyorumlar"
    )  # ? eşleştirme, tabloda yazan_id yazan -> yyroumlar
    yazi = models.ForeignKey(
        YazilarModel, on_delete=models.CASCADE, related_name="yorumlar"
    )  # ? her yorum yazıyla eşleştirilecek / yazinin -> yorumlar ına erişmek
    yorum = models.TextField()
    # olusturulma_tarihi = models.DateTimeField(auto_now=False, auto_now_add=True)
    # duzenlenme_tarihi = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "yorum"
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"

    def __str__(self):
        return (
            self.yazan.username
        )  # üstteki alanıda değiştirir the yorum selcuk added successfuly
