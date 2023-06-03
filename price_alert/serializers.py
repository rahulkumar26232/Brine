from rest_framework.serializers import ModelSerializer

from price_alert.models import PriceAlert, Currency


class CurrencyModelSerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class PriceAlertModelSerializer(ModelSerializer):
    currency = CurrencyModelSerializer()

    class Meta:
        model = PriceAlert
        fields = ['id', 'target_price', 'status', 'created_at', 'currency']
