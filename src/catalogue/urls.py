from django.urls import path

from catalogue.views import test_view


app_name = 'catalogue'

urlpatterns = [
    path('', test_view, name='index'),
    path('books/<id>', test_view, name='book-detail'),
    path('authors/<id>', test_view, name='author-detail')
]
