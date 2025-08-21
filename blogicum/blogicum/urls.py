from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # маршруты приложения blog
    path('', include('blog.urls')),

    # маршруты приложения pages
    path('', include('pages.urls')),
]
