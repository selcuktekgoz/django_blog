from django.contrib import admin
from blog.models import KategoriModel, YazilarModel

admin.site.register(KategoriModel)  # ? admin panael de göstermek için
admin.site.register(YazilarModel)
