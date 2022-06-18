


APR (Annual Percentage Rate) is one of the most crucial factors to consider for optimal efficiency. Staking reward comprehensively includes income from inflation and transaction fee distribution. We will  try to explain the mechanism of APR: the inflation income of staking profit.

## What is APR?
In staking crypto-currency, users are always keen to the most secure, efficient, highest-income-guaranteed investment route. APR is the most intuitive, important key element in staking because it presents how much interest a user would receive for the bonded asset in one year.

Simply put, your staking APR is calculated as below:

    [Inflation * (1-Community Tax)] / Bonded Tokens Ratio

Sometimes, instead of inflation per block we have Epochs ,daily distribution mechanism, it is  using in Osmo and Evmos currently.

In this case, all inflation/user rewards will be distributed in exact time once per day.

Let's go to some formulas, according to networks:

---
#### Juno/Cosmos based  blockchains:



    [Inflation * (1-Community Tax)] / Bonded Tokens Ratio
    
Inflation: https://lcd.juno-1.bronbro.io/cosmos/mint/v1beta1/inflation

Community Tax: https://lcd.juno-1.bronbro.io/cosmos/distribution/v1beta1/params

Bonded Tokens Ratio = Bonded tokens / Current Supply

Bonded tokens: https://lcd.juno-1.bronbro.io/cosmos/staking/v1beta1/pool

Current Supply: https://lcd.juno-1.bronbro.io/cosmos/bank/v1beta1/supply/ujuno

According to this formula we will get ideal APR. We assume, that blocks will be produced       every 5 secs, but in real life, it gets ~6 secs, so this formula need to be adjusted with blockchain time producing.

To calculate real APR, formula should be adjusted:

    [Inflation * (1-Community Tax)] / Bonded Tokens Ratio * 5 /average block time  

Average block time : Average time per 1000 blocks

You can get actual data, from [link](https://supply-api.junonetwork.io/), provided by Juno devs.

You can use this formula for most Cosmos base chains.

Now let's see how Epoch chains works.

---

#### Osmosis blockchain: 

You can find more information about this  in [medium article](https://medium.com/osmosis/osmo-token-distribution-ae27ea2bb4db)

According to it, each epoch, 750 000 tokens will be distributed between delegators and liquidity pool providers.

This number will be decreased soon to 502 500.

APR can be calculated easy in this way:

    epoch_provisions * staking_share * 365 / bonded_tokens_amount

epoch_provisions: https://lcd.osmosis-1.bronbro.io/osmosis/mint/v1beta1/epoch_provisions

staking_share:  0.25 const

bonded_tokens_amount: https://lcd.osmosis-1.bronbro.io/cosmos/staking/v1beta1/pool
   

---

#### Evmos blockchain:

Evmos has also [medium article](https://medium.com/evmos/the-evmos-token-model-edc07014978b), how to calculate APR:

    APR = (365 * EpochProvision * StakingRewards factor) / Bonded tokens

More information can be found here : 

Epoch provision: https://lcd.evmos-9001-2.bronbro.io/evmos/inflation/v1/epoch_mint_provision 

Staking rewards factor: https://lcd.evmos-9001-2.bronbro.io/evmos/inflation/v1/params 

Bonded tokens:  https://lcd.evmos-9001-2.bronbro.io/cosmos/staking/v1beta1/pool

---

#### Crescent blockchain:

    liquidstaking.total_reward_ucre_amount_per_year / liquidstaking.total_liquid_tokens

You can get this data from: https://apigw.crescent.network/params

This is an official crescent API.

More information can be find [here](https://docs.crescent.network/introduction/liquid-staking/overview-of-staking-rewards)

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

