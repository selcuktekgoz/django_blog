from django.urls import path, include
from blog.views import iletisim

urlpatterns = [path("", iletisim), path("iletisim/", iletisim)]
