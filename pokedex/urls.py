from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.predict_pokemon, name="index"),
]

urlpatterns += staticfiles_urlpatterns()