# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> tokenB->tokenA amountIn:5 amountOut:5.655321988655323
  tokenA->tokenE amountIn:5.655321988655323 amountOut: 1.0583153138066888
  tokenE->tokenD amountIn:1.0583153138066888 amountOut:2.429786260142227
  tokenD->tokenC amountIn:2.4297862601422275 amountOut:5.038996197252912
  tokenC->tokenB amountIn:5.038996197252912 amountOut:20.04233958918818
  final_reward: 20.04233958918818

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage in AMMs refers to the difference between the expected price of a trade and the price at which the trade is actually executed. This discrepancy can occur due to large orders affecting the price in the liquidity pool. Uniswap V2 addresses slippage by using the constant product formula x * y = k, where x and y represent the reserve amounts of each token, and k is a constant. As trades occur, the reserve levels change to maintain the constancy of k, which in turn ensures that prices move with trade size. This natural price movement inherently limits slippage.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> The mint function in the UniswapV2Pair contract, which is used to create new liquidity tokens, subtracts a minimum liquidity upon the initial liquidity provision to prevent division by zero and to ensure there is a sufficient token balance within the contract for it to function effectively. This minimum liquidity is also sent to the zero address, effectively locking away a portion of the initial liquidity permanently, thus preventing the pool from being completely drained when all liquidity is removed and maintaining basic stability within the system.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> In the mint function of the UniswapV2Pair contract, when depositing tokens (not for the first time), liquidity can only be obtained using a specific formula to ensure the distribution of liquidity tokens is proportional to the current pool's reserves. This proportionality maintains the pool's ratio constant, ensuring that investors' shares are proportional to their contribution and preventing the dilution or augmentation of existing liquidity providers' shares.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> A sandwich attack is a trading manipulation strategy where an attacker sees a pending substantial trade and places two trades around it—one before and one after. This way, the attacker can increase the price before the original trade and decrease it afterward, profiting in the process. When initiating a swap, if an attacker can execute trades on the blockchain before and after your trade, you may end up buying tokens at an inflated price, and the attacker's subsequent trade could cause the price to drop, diminishing the value of your trade.

