
from django.contrib import admin
from django.urls import path
from simpleApp.views import hello


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello.as_view(),name="home"),
]
