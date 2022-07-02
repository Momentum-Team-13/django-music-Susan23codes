"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from albums import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_albums, name='show_albums'),
    path('album/add', views.add_album, name='add_album'),
    path('album/<int:pk>/detail', views.album_detail, name='album_detail'),
    path('album/<int:pk>/edit', views.edit_album, name='edit_album'),
    path('album/<int:pk>/delete', views.delete_album, name='delete_album')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
