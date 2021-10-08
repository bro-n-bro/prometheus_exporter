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
                juno_price = api_calls.get_price()
                value = CounterMetricFamily("Juno_PRICE", 'Juno PRICE', labels='value')
                value.add_metric(["juno_price"], juno_price)
                yield value
                juno_community_pool = api_calls.pool()
                value1 = CounterMetricFamily("Juno_POOL", 'Juno Community POOL', labels='value')
                value1.add_metric(["juno_community_pool"], juno_community_pool)
                yield value1
                juno_bonded_tokens = api_calls.bonded_tokens()
                value2 = GaugeMetricFamily("Juno_BONDED_TOKEN", 'Juno TOKEN ', labels = 'value')
                value2.add_metric(["juno_bonded_tokens"], juno_bonded_tokens)
                yield value2
                juno_unbonded_tokens = api_calls.unbonded_tokens()
                value3 = GaugeMetricFamily("Juno_UNBONDED_TOKEN", 'Juno UnTOKEN ', labels = 'value')
                value3.add_metric(["juno_unbonded_tokens"], juno_unbonded_tokens)
                yield value3
                juno_inflation = api_calls.get_inflation()
                value4 = GaugeMetricFamily("Juno_INFLATION", 'Juno INFLATION ', labels = 'value')
                value4.add_metric(["juno_inflation"], juno_inflation)
                yield value4
                juno_height = api_calls.height()
                value5 = GaugeMetricFamily("Juno_HEIGHT", 'Juno HEIGHT ', labels = 'value')
                value5.add_metric(["juno_height"], juno_height)
                yield value5
                juno_supply = api_calls.supply()
                value7 = GaugeMetricFamily("Juno_SUPPLY", 'Juno SUPPLY ', labels = 'value')
                value7.add_metric(["juno_supply"], juno_supply)
                yield value7
                juno_apr = api_calls.get_apr()
                value6 = GaugeMetricFamily("Juno_APR", 'Juno Apr ', labels = 'value')
                value6.add_metric(["juno_apr"], juno_apr)
                yield value6
                juno_amount_bonded_ratio = api_calls.get_amount_bonded_ratio()
                value8 = GaugeMetricFamily("Juno_Bonded_Ratio", 'Juno bonded ration', labels = 'value')
                value8.add_metric(["juno_amount_bonded_ratio"], juno_amount_bonded_ratio)
                yield value8
                juno_gov_open = api_calls.gov_open_prop()
                value9 = CounterMetricFamily("Juno_GOV_OPEN_PROPOSALS", 'Juno GOV', labels='value')
                value9.add_metric(["juno_gov_open"], juno_gov_open)
                yield value9
                juno_gov_deposit = api_calls.gov_deposit_prop()
                value10 = GaugeMetricFamily("Juno_GOV_DEPOST_PROPOSALS", 'Juno GOV', labels = 'value')
                value10.add_metric(["juno_gov_deposit"], juno_gov_deposit)
                yield value10
                juno_market_cap = api_calls.get_market_cap()
                value12 = GaugeMetricFamily("Juno_Market_Cap", 'Juno MC', labels = 'value')
                value12.add_metric(["juno_market_cap"], juno_market_cap)
                yield value12
                juno_circulating_supply = api_calls.get_circulating_supply()
                value12 = GaugeMetricFamily("Juno_Circulating_Supply", 'Juno Circ Supply', labels = 'value')
                value12.add_metric(["juno_circulating_supply"], juno_circulating_supply)
                yield value12




if __name__ == '__main__':
        start_http_server(8010)         ## port where metrics need to be exposed.
        REGISTRY.register(CustomCollector())
        while True:
                time.sleep(5)
