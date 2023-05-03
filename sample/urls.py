from django.contrib import admin
from django.urls import path, include

import polls.views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", polls.views.index, name='index'),
    path("index.html", polls.views.index, name='index'),
    path("detail.html", polls.views.detail, name='detail'),
]
