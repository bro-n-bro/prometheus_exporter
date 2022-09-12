


APR (Annual Percentage Rate) is one of the most crucial factors to consider for optimal efficiency. Staking reward comprehensively includes income from inflation and transaction fee distribution. We will  try to explain the mechanism of APR: the inflation income of staking profit.

## What is APR?
In staking crypto-currency, users are always keen to the most secure, efficient, highest-income-guaranteed investment route. APR is the most intuitive, important key element in staking because it presents how much interest a user would receive for the bonded asset in one year.

Your staking APR is calculated as below:

    [inflation * (1- community_tax)] / bonded_tokens_ratio
    


 It is possible to simplify APR equation in general if:
```
inflation_rate = annual_provisions / total_supply
```

where `annual_provisions` is usually available by the  `/cosmos/mint/v1beta1/annual_provisions`  endpoint and `total_supply` - `/cosmos/bank/v1beta1/supply` endpoint

```
bonded_tokens_ratio = bonded_tokens_amount / total_supply
```

where `bonded_tokens_amount` can be find here: `/cosmos/staking/v1beta1/pool`

The general APR equation can be:

```
APR = annual_provisions * (1 - community_tax) / bonded_tokens_amount
```

where `community_tax` is the chain parameter `/cosmos/distribution/v1beta1/params` 


This way we can unify epoch and non-epoch networks:


For epoch networks the  `annual_provisions`  is

```
annual_provisions = epoch_provisions * 365.3
```
The general APR for Epoch chains is:

```
APR = annual_provisions * (1 - community_tax) / bonded_tokens_amount
```



---
#### Non-epoch Cosmos based  blockchains:


```
APR = annual_provisions * (1 - community_tax) / bonded_tokens_amount
```

According to this formula we will get ideal APR. We assume, that blocks will be produced       every 5 secs, but in real life, it cat be created longer, so this formula need to be adjusted with blockchain time producing.

To calculate real APR, formula should be adjusted with `correction_annual_coefficient`:

This is an relation between `real_blocks_per_year` and `block_per_year` in params

```
correction_annual_coefficient = real_blocks_per_year / block_per_year
```

where

```
real_blocks_per_year = 31561920 / real_block_time
```

and

```
real_block_time = time_for_n_blocks / n
```

so, the final equation for non-epoch networks APR is

```
APR = (annual_provisions * (1 - community_tax) / bonded_tokens_amount) * correction_annual_coefficient

```


You can use this formula for most Cosmos base chains.

Now let's see how Epoch chains works.

---

#### Osmosis blockchain: 

You can find more information about this  in [medium article](https://medium.com/osmosis/osmo-token-distribution-ae27ea2bb4db)

APR can be calculated easy in this way:

    APR = annual_provisions * staking_rewards_factor / bonded_tokens_amount

where

``epoch_provisions: https://lcd.osmosis-1.bronbro.io/osmosis/mint/v1beta1/epoch_provisions
``

``
annual_provisions = epoch_provisions * 365.3
``

``
staking_rewards_factor:  0.25 const
``

`` bonded_tokens_amount: https://lcd.osmosis-1.bronbro.io/cosmos/staking/v1beta1/pool
``

``
  community_tax: https://lcd.osmosis-1.bronbro.io/cosmos/distribution/v1beta1/params 
``

---

#### Evmos blockchain:

Evmos has also [medium article](https://medium.com/evmos/the-evmos-token-model-edc07014978b), how to calculate APR:

    APR = annual_provisions * staking_rewards_factor / bonded_tokens_amount

More information can be found here : 

``Epoch provision: https://lcd.evmos-9001-2.bronbro.io/evmos/inflation/v1/epoch_mint_provision
``

``Staking rewards factor: https://lcd.evmos-9001-2.bronbro.io/evmos/inflation/v1/params 
``

``Bonded tokens:  https://lcd.evmos-9001-2.bronbro.io/cosmos/staking/v1beta1/pool
``

``
community_tax: https://lcd.evmos-9001-2.bronbro.io/cosmos/distribution/v1beta1/params
``

---

#### Crescent blockchain:

    liquidstaking.total_reward_ucre_amount_per_year / bonded tokens

where

``bonded tokens: https://lcd.crescent-1.bronbro.io/cosmos/staking/v1beta1/pool
``

``liquidstaking.total_reward_ucre_amount_per_year: https://apigw.crescent.network/params
``

This is an official crescent API.

More information can be find [here](https://docs.crescent.network/introduction/liquid-staking/overview-of-staking-rewards)

---

#### Stride blockchain:

You can calculate APR for Stride network:

    APR = annual_provisions * staking / bonded_tokens_amount

More information can be found here : 

``genesis_epoch_provisions: https://lcd.stride-1.bronbro.io/mint/v1beta1/params
``

``annual_provisions = genesis_epoch_provisions * reduction_period_in_epochs
``

``staking: https://lcd.stride-1.bronbro.io/mint/v1beta1/params
``

``Bonded tokens:  https://lcd.stride-1.bronbro.io/cosmos/staking/v1beta1/pool
``

---
Reference:

LCD endpoints:

https://lcd.bostrom.bronbro.io

https://lcd.crescent-1.bronbro.io

https://lcd.gravity-bridge-3.bronbro.io

https://lcd.juno-1.bronbro.io

https://lcd.microtick-1.bronbro.io

https://lcd.omniflixhub-1.bronbro.io

https://lcd.osmosis-1.bronbro.io

https://lcd.stargaze-1.bronbro.io

https://lcd.emoney-3.bronbro.io

https://lcd.evmos-9001-2.bronbro.io



Stargaze: https://supply-api.publicawesome.dev/

Juno: https://supply-api.junonetwork.io/

