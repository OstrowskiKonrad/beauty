from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Portfolio(TemplateView):
    template_name = "portfolio.html"


class Clients(TemplateView):
    template_name = "clients.html"


class Offer(TemplateView):
    template_name = "offer.html"
