from django.apps import AppConfig


class PriceAlertConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'price_alert'

    def ready(self):
        from price_alert.models import Currency
        obj, _ = Currency.objects.get_or_create(name='Bitcoin', symbol='btc')

        # TODO : fill currency using fixture

        from price_alert.tasks import currency_dict
        currency_dict[obj.name] = obj.pk
