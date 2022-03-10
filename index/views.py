from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    """ Главная страница сайта """
    # Тут будет главная страница сайта и расположение товаров
    template_name = 'index/index.html'