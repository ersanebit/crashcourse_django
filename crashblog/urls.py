from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps

from core.views import robots_txt

from .sitemaps import CategorySitemap, PostSitemap

from core.views import frontpage, about

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name = 'django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('blog.urls')),
    path('', frontpage, name='frontpage')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
