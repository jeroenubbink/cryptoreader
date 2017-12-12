import json

import requests

from redis_cache import cache_it_json

class CoinCapClient(object):

    def __init__(self, coin):
        self.coin = coin
        self.base_url = 'http://coincap.io/'
        self.base_coin_url = self.base_url + 'page/'

    @cache_it_json(expires=60*5)
    def get_price_details(self):
        resp = requests.get(self.base_coin_url + self.coin)
        if resp.status_code != 200:
            return {'ERROR': 'ERROR status_code {} trying to connect to the CoinCap API'.format(resp.status_code)}
        return resp.json()
