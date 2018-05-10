from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


class HistoriaView(TemplateView):

    template_name = 'page/historia.html'

   
