from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin

from price_alert.models import PriceAlert
from price_alert.serializers import PriceAlertModelSerializer


class PriceAlertFetchApi(ListModelMixin,viewsets.GenericViewSet):
    serializer_class = PriceAlertModelSerializer

    def get_queryset(self):
        status_filter = self.request.query_params.get("status")
        alerts = PriceAlert.objects.filter(user=self.request.user).select_related("currency")

        if status_filter:
            alerts = alerts.filter(status=status_filter)

        return alerts






