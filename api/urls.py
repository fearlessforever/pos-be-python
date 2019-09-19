from django.urls import path

from api.views import tes

urlpatterns = [
    path('', tes.index, name='index'),
]