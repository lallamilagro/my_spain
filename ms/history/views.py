from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


class HistoryView(TemplateView):

    template_name = 'page/history.html'

   
