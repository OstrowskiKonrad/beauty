from django.urls import path
from .views import HomePageView, About, Portfolio, Clients, Offer

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path("portfolio/", Portfolio.as_view(), name="portfolio"),
    path("klientki/", Clients.as_view(), name="clients"),
    path("oferta/", Offer.as_view(), name="offer"),
]
