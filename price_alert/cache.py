from abc import ABC

import redis

from Brine import settings

REDIS_INSTANCE = redis.from_url(url=settings.REDIS_URI, decode_responses=True)


class PriceAlertCache:
    key = 'price_{}_currency_{}_alert'

    @classmethod
    def get(cls, price: int, currency_id: int):
        return REDIS_INSTANCE.get(cls.key.format(price, currency_id))

    @classmethod
    def set(cls, price: int, currency_id: int):
        REDIS_INSTANCE.set(cls.key.format(price, currency_id),0)

    @classmethod
    def delete(cls, price: int, currency_id: int):
        REDIS_INSTANCE.delete(cls.key.format(price, currency_id))

