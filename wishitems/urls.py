from django.urls import path
from . import views

urlpatterns = [
    path("wishlist/", views.wishlist, name="wishlist"),
    path(
        "wishlist/<int:wishitem_id>/", views.wishlist_retriev, name="wishlist_retriev"
    ),
]
