from django.db import models
from django.contrib.auth.models import AbstractUser


# ? blank ->  yüklemeyebiliriz, null -> db dede boş kayıt oluşabilsin.
class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"

    def __str__(self):
        return self.username


#! migrate etmeden önce bunu kullanacağımı settingste belirt
#! migrate edince sqlite tekrar sil sonra migrate et hata veriyor
