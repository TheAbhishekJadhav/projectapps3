from django.urls import path
from . import views

urlpatterns = [
    path('assets', views.AssetView.as_view(), name='assets'),
    path('bookings/get', views.GetBookingView.as_view(), name='getbookings'),
    path('bookings/add', views.AddBookingView.as_view(), name='addbooking'),
    path('assetbookings', views.GetAssetBookingView.as_view(), name='assetbookings')
]