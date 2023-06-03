from django.urls import path

from price_alert.apis.create import PriceAlertCreateApi
from price_alert.apis.delete import PriceAlertDeleteApi
from price_alert.apis.filter import PriceAlertFetchApi

urlpatterns = [
    path('create/', PriceAlertCreateApi.as_view(),),
    path('fetch/', PriceAlertFetchApi.as_view({'get': 'list'}),),
    path('delete/<int:id>/', PriceAlertDeleteApi.as_view(), ),
]
