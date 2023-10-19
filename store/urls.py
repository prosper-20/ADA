from django.urls import path
from .views import ProductDetailPage, ProductHomePage


urlpatterns = [
    path("", ProductHomePage.as_view(), name="home"),
    path("<slug:slug>/", ProductDetailPage.as_view(), name="detail")
]