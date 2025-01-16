from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel

admin.site.register(KategoriModel)  # ? admin panael de göstermek için


@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ("baslik", "icerik")
    list_display = ("baslik", "olusturulma_tarihi", "duzenlenme_tarihi")


# admin.site.register(YazilarModel, YazilarAdmin)


class YorumAdmin(admin.ModelAdmin):
    search_fields = ("yazan__username", "yorum")
    list_display = ("yazan", "olusturulma_tarihi", "duzenlenme_tarihi")


admin.site.register(YorumModel, YorumAdmin)


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("email", "olusturulma_tarihi")
