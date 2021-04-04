from django.urls import include
from django.urls import path
from django.views.generic import RedirectView


app_name = 'library'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='library:catalogue:index', permanent=False), name='index'),
    path('catalogue/', include('catalogue.urls', namespace='catalogue'), name='catalogue'),
]
