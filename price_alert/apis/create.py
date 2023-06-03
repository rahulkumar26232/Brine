from django.http import JsonResponse
from rest_framework.views import APIView

from price_alert.cache import PriceAlertCache
from price_alert.models import PriceAlert


class PriceAlertCreateApi(APIView):

    def post(self, request):
        if 'target_price' not in request.data:
            return JsonResponse({'message': 'please provide target price for the alert'})
        if 'currency_id' not in request.data:
            return JsonResponse({'message': 'please provide currency for the alert'})

        target_price = request.data['target_price']
        currency_id = request.data['currency_id']

        PriceAlert.objects.create(user=request.user,target_price=target_price,currency_id=currency_id)

        if not PriceAlertCache.get(price=target_price,currency_id=currency_id):
            PriceAlertCache.set(price=target_price, currency_id=currency_id)

        return JsonResponse({'message': 'alert created successfully'})
