"""
URL configuration for Cafetera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    # Path admin
    path('admin/', admin.site.urls),
    # Path core
    path('', include('core.urls')),
    # Path service
    path('services/', include('Services.urls')),
    # Path blog
    path('blog/', include("blog.urls")),
    # Path pages
    path("page/", include("pages.urls")),
    # Path contact
    path("contact/", include("contact.urls")),
    # Path store
    path("store/", include("store.urls"))
]
