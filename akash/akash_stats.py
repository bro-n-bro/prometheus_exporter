import api_calls
import random
import time
import requests
import json
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily, SummaryMetricFamily, InfoMetricFamily
from prometheus_client import start_http_server, Summary, Info
# Create a metric to track time spent and requests made.
class CustomCollector(object):     ## Class for CustomCollector which helps us  to use different metric types
        def __init__(self):
                pass
        def collect(self):
                akash_price = api_calls.price()
                value = CounterMetricFamily("Akash_PRICE", 'Akash PRICE', labels='value')
                value.add_metric(["akash_price"], akash_price)
                yield value
                akash_community_pool = api_calls.pool()
                value1 = CounterMetricFamily("Akash_POOL", 'Akash Community POOL', labels='value')
                value1.add_metric(["akash_community_pool"], akash_community_pool)
                yield value1
                akash_bonded_tokens = api_calls.bonded_tokens()
                value4 = GaugeMetricFamily("Akash_BONDED_TOKEN", 'Akash TOKEN ', labels = 'value')
                value4.add_metric(["akash_bonded_tokens"], akash_bonded_tokens)
                yield value4
                akash_unbonded_tokens = api_calls.unbonded_tokens()
                value5 = GaugeMetricFamily("Akash_UNBONDED_TOKEN", 'Akash TOKEN ', labels = 'value')
                value5.add_metric(["akash_unbonded_tokens"], akash_unbonded_tokens)
                yield value5
                akash_inflation = api_calls.inflation()
                value6 = GaugeMetricFamily("Akash_INFLATION", 'Akash INFLATION ', labels = 'value')
                value6.add_metric(["akash_inflation"], akash_inflation)
                yield value6
                akash_height = api_calls.height()
                value7 = GaugeMetricFamily("Akash_HEIGHT", 'Akash HEIGHT ', labels = 'value')
                value7.add_metric(["akash_height"], akash_height)
                yield value7
                akash_block_time = api_calls.block_time()
                value8 = GaugeMetricFamily("Akash_BLOCK", 'Akash BLOCK ', labels = 'value')
                value8.add_metric(["akash_block"], akash_block_time)
                yield value8



if __name__ == '__main__':
        start_http_server(8001)         ## port where metrics need to be exposed.
        REGISTRY.register(CustomCollector())
        while True:
                time.sleep(10)
