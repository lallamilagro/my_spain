from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


class ArticlesView(TemplateView):

    template_name = 'page/articles.html'

   
