import requests
import json

def pool():
   pool = requests.get('https://api-akash.cosmostation.io/v1/status')
   community_pool = pool.json()["community_pool"][0]["amount"]
   return (community_pool)

def trx():
   trx = requests.get('https://api-akash.cosmostation.io/v1/status')
   trx_count = trx.json()["total_txs_num"]
   return (trx_count)

def gov_open_prop():
   gov = requests.get('http://LCD_ENDPOINT/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   open_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_VOTING_PERIOD":
                  open_count = open_count + 1

   return (open_count)

def gov_deposit_prop():
   gov = requests.get('http://LCD_ENDPOINT/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   deposit_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_DEPOSIT_PERIOD":
                  deposit_count = deposit_count + 1
   return (deposit_count)

def price():
   price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=akash-network&vs_currencies=usd')
   data = price.json()['akash-network']['usd']
   return (data)

def bonded_tokens():
   tokens = requests.get('https://api-akash.cosmostation.io/v1/status')
   bonded_tokens = tokens.json()['bonded_tokens']
   return (bonded_tokens)

def unbonded_tokens():
   tokens = requests.get('https://api-akash.cosmostation.io/v1/status')
   unbonded_tokens = tokens.json()['not_bonded_tokens']
   return (unbonded_tokens)

def inflation():
   inflation = requests.get('http://LCD_ENDPOINT/cosmos/mint/v1beta1/inflation')
   inflation_total = inflation.json()['inflation']
   return (inflation_total)

def height():
   height = requests.get('https://api-akash.cosmostation.io/v1/status')
   data = height.json()['block_height']
   return (data)
def block_time():
   block_time = requests.get('https://api-akash.cosmostation.io/v1/status')
   data = block_time.json()['block_time']
   return (data)
