from django.urls import path

from . import views

urlpatterns = [
    path('', views.HistoriaView.as_view(), name='historia'),
]

