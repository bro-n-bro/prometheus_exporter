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
                cosmos_price = api_calls.price()
                value = CounterMetricFamily("COSMOS_PRICE", 'Cosmos PRICE', labels='value')
                value.add_metric(["cosmos_price"], cosmos_price)
                yield value
                community_pool = api_calls.pool()
                value1 = CounterMetricFamily("Cosmos_POOL", 'Cosmos Community POOL', labels='value')
                value1.add_metric(["cosmos_community_pool"], community_pool)
                yield value1
                bonded_tokens = api_calls.bonded_tokens()
                value2 = GaugeMetricFamily("Cosmos_BONDED_TOKEN", 'Cosmos TOKEN ', labels = 'value')
                value2.add_metric(["cosmos_bonded_tokens"], bonded_tokens)
                yield value2
                unbonded_tokens = api_calls.unbonded_tokens()
                value3 = GaugeMetricFamily("Cosmos_UNBONDED_TOKEN", 'Cosmos UnTOKEN ', labels = 'value')
                value3.add_metric(["cosmos_unbonded_tokens"], unbonded_tokens)
                yield value3
                inflation = api_calls.inflation()
                value4 = GaugeMetricFamily("Cosmos_INFLATION", 'Cosmos INFLATION ', labels = 'value')
                value4.add_metric(["cosmos_inflation"], inflation)
                yield value4
                supply = api_calls.supply()
                value7 = GaugeMetricFamily("Cosmos_SUPPLY", 'Cosmos SUPPLY ', labels = 'value')
                value7.add_metric(["cosmos_supply"], supply)
                yield value7
                gov_open = api_calls.gov_open_prop()
                value9 = CounterMetricFamily("Cosmos_GOV_OPEN_PROPOSALS", 'Cosmos GOV', labels='value')
                value9.add_metric(["cosmos_gov_open"], gov_open)
                yield value9
                gov_deposit = api_calls.gov_deposit_prop()
                value10 = GaugeMetricFamily("Cosmos_GOV_DEPOST_PROPOSALS", 'Cosmos GOV', labels = 'value')
                value10.add_metric(["cosmos_gov_deposit"], gov_deposit)
                yield value10
                apr = api_calls.get_apr()
                value13 = GaugeMetricFamily("Cosmos_APR", 'Cosmos APR', labels = 'value')
                value13.add_metric(["apr"], apr)
                yield value13
                cosmos_market_cap = api_calls.get_market_cap()
                value14 = GaugeMetricFamily("Cosmos_Market_Cap", 'COsmos MC', labels = 'value')
                value14.add_metric(["cosmos_market_cap"], cosmos_market_cap)
                yield value14
                cosmos_circulating_supply = api_calls.get_circulating_supply()
                value15 = GaugeMetricFamily("Cosmos_Circulating_Supply", 'Cosmos Circ Supply', labels = 'value')
                value15.add_metric(["cosmos_circulating_supply"], cosmos_circulating_supply)
                yield value15
                cosmos_amount_bonded_ratio = api_calls.get_amount_bonded_ratio()
                value16 = GaugeMetricFamily("Cosmos_Bonded_Ratio", 'Cosmos bonded ration', labels = 'value')
                value16.add_metric(["cosmos_amount_bonded_ratio"], cosmos_amount_bonded_ratio)
                yield value16








if __name__ == '__main__':
        start_http_server(8003)         ## port where metrics need to be exposed.
        REGISTRY.register(CustomCollector())
        while True:
                time.sleep(90)
