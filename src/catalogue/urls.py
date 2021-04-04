from django.urls import path

from catalogue.views import test_view


app_name = 'catalogue'

urlpatterns = [
    path('', test_view, name='index'),
]
