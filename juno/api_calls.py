import requests
import json

def gov_open_prop():
   gov = requests.get('LCD_ENDPOINT/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   open_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_VOTING_PERIOD":
                  open_count = open_count + 1

   return (open_count)

def gov_deposit_prop():
   gov = requests.get('LCD_ENDPOINT/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   deposit_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_DEPOSIT_PERIOD":
                  deposit_count = deposit_count + 1
   return (deposit_count)


def pool() -> float:
   pool = requests.get('LCD_ENDPOINT/cosmos/distribution/v1beta1/community_pool')
   community_pool = pool.json()['pool'][0]['amount']
   return float(community_pool)

def get_price()-> float:
   price = requests.get('https://api-osmosis.imperator.co/tokens/v1/price/JUNO')
   data = price.json()['price']
   return float(data)

def bonded_tokens() -> int:
   tokens = requests.get('LCD_ENDPOINT/cosmos/staking/v1beta1/pool')
   bonded_tokens = tokens.json()['pool']['bonded_tokens']
   return int(bonded_tokens)

def unbonded_tokens():
   tokens = requests.get('LCD_ENDPOINT/cosmos/staking/v1beta1/pool')
   unbonded_tokens = tokens.json()['pool']['not_bonded_tokens']
   return (unbonded_tokens)

def get_inflation() -> float:
   data = requests.get('LCD_ENDPOINT/cosmos/mint/v1beta1/inflation').json()
   return float(data['inflation'])

def height():
   height =  requests.get('LCD_ENDPOINT/blocks/latest')
   data = height.json()['block']['header']['height']
   return (data)


def supply() -> int:
   supply = requests.get('LCD_ENDPOINT/cosmos/bank/v1beta1/supply')
   data = supply.json()['supply']
   for i in data:
      if  i['denom'] == 'ujuno':
         return int(i['amount'])

def get_circulating_supply() -> float:
    total_supply = supply()
    total_pool = pool()
    return total_supply / 1000000 - total_pool / 1000000 - 1782312 - 10084396 - 2373341 + 422001 #Total Supply minus ( community pool + core team (Vested) + core development vested + JunoHacks)

def get_market_cap():
    total_price = get_price()
    return total_price * get_circulating_supply()

def get_apr():
    total_supply = supply()
    infl = get_inflation()
    bond_tokens = bonded_tokens()
    return total_supply * infl / bond_tokens * 100

def get_amount_bonded_ratio():
    bond_tokens = bonded_tokens()
    total_supply = supply()
    return bond_tokens / total_supply * 100
