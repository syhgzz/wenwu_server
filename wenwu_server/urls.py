"""
URL configuration for wenwu_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


#url.py
from django.contrib import admin
from django.urls import path
import line_app.views
import frontend_app.views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',line_app.views.movieViews.as_view()),
    path('process_file/',line_app.views.process_file,name='process_file'),

    #前端路由, 给出一个前端例子
    path('', frontend_app.views.frontend, name='frontend'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

