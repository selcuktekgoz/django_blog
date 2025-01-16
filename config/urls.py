from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("blog/", include("blog.urls")),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # settings.MEDIA_URL den sonra settings.MEDIA_ROOT yorumla. url de baş kısım gözükecek
