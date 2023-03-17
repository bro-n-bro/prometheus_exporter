def gov_open_prop():
   gov = requests.get('https://lcd.cosmoshub-4.bronbro.io/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   open_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_VOTING_PERIOD":
                  open_count = open_count + 1

   return (open_count)

def gov_deposit_prop():
   gov = requests.get('https://lcd.cosmoshub-4.bronbro.io/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   deposit_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_DEPOSIT_PERIOD":
                  deposit_count = deposit_count + 1
   return (deposit_count)


def pool()-> float:
   pool = requests.get('https://lcd.cosmoshub-4.bronbro.io/cosmos/distribution/v1beta1/community_pool')
   community_pool = pool.json()['pool'][2]['amount']
   return float(community_pool)

def price()-> float:
   price = requests.get('https://api-osmosis.imperator.co/tokens/v2/price/ATOM')
   data = price.json()['price']
   return float(data)


def bonded_tokens() -> float:
   tokens = requests.get('https://lcd.cosmoshub-4.bronbro.io/cosmos/staking/v1beta1/pool')
   bonded_tokens = tokens.json()['pool']['bonded_tokens']
   return float(bonded_tokens)

def unbonded_tokens():
   tokens = requests.get('https://lcd.cosmoshub-4.bronbro.io/cosmos/staking/v1beta1/pool')
   unbonded_tokens = tokens.json()['pool']['not_bonded_tokens']
   return (unbonded_tokens)

def inflation() -> float:
   inflation = requests.get('https://lcd.cosmoshub-4.bronbro.io/cosmos/mint/v1beta1/inflation')
   inflation_total = inflation.json()['inflation']
   return float(inflation_total)


def supply() -> float:
   supply = requests.get('https://lcd.cosmoshub-4.bronbro.io/cosmos/bank/v1beta1/supply/uatom')
   data = supply.json()['amount']['amount']
   return float(data)

def get_apr():
    total_supply = supply()
    infl = inflation()
    bond_tokens = bonded_tokens()
    return infl * (1 - (2 / 100)) / (bond_tokens/total_supply)

def get_circulating_supply():
    total_supply = supply()
    community_pool =  pool()
    return (total_supply - community_pool)/ 1000000

def get_market_cap():
    total_price = price()
    return total_price * get_circulating_supply()

def get_amount_bonded_ratio():
    bond_tokens = bonded_tokens()
    total_supply = supply()
    return bond_tokens / total_supply * 100
