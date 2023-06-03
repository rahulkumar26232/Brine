from price_alert.models import PriceAlert


def price_alert_fetch(price: int, currency_id: int) -> list[PriceAlert]:
    return PriceAlert.objects.filter(target_price=price, currency=currency_id,
                                     status=PriceAlert.TextChoices.created).select_related("user")

