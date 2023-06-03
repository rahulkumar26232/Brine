from celery import shared_task

from price_alert.cache import PriceAlertCache
from price_alert.models import PriceAlert
from price_alert.selector import price_alert_fetch
from price_alert.services import fetch_new_prices

currency_dict = {}

@shared_task
def fetch_latest_crypto_price():
    currency_prices: dict = fetch_new_prices()

    for data in currency_prices:
        if data['name'] in currency_dict and PriceAlertCache.get(price=data['current_price'],
                                                                 currency_id=currency_dict[data['name']]):

            alerts: list[PriceAlert] = price_alert_fetch(price=data['current_price'],
                                                         currency_id=currency_dict[data['name']])

            PriceAlertCache.delete(price=data['current_price'],currency_id=currency_dict[data['name']])

            if alerts:
                for alert in alerts:
                    notify_user_for_matching_target_price.apply_async(kwargs={'email_id': alert.user.email})

                alerts.update(status=PriceAlert.TextChoices.triggered)


@shared_task(queue='email_queue')
def notify_user_for_matching_target_price(email_id: str):
    message = '''
                Dear User,
                    
                    This notification is regarding that current price of BTC hit the Trigger Price set by you
                '''

    print(message)
