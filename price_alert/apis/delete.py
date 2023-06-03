from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from price_alert.cache import PriceAlertCache
from price_alert.models import PriceAlert
from price_alert.selector import price_alert_fetch


class PriceAlertDeleteApi(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id: int):

        try:
            alert = PriceAlert.objects.get(pk=id, user_id=request.user.pk)
        except ObjectDoesNotExist:
            return Response({'message': 'invalid alarm id'})

        if alert.status == PriceAlert.TextChoices.created:
            alert.status = PriceAlert.TextChoices.deleted
            alert.save()

        if not price_alert_fetch(price=alert.target_price,currency_id=alert.currency_id).exists():

            PriceAlertCache.delete(price=alert.target_price,currency_id=alert.currency_id)

        return Response({'message': 'alarm deleted successfully'}, status=HTTP_204_NO_CONTENT)
