# Crude Oil Futures P&L Example

## Purpose

This example shows how a basic crude oil futures position creates profit or loss depending on whether the trader is long or short.

## Contract

| Item | Value |
|---|---:|
| Contract | WTI Crude Oil Futures |
| Unit | Barrels |
| Contract size | 1,000 barrels |
| Price unit | Dollars per barrel |

## Example 1: Long WTI Futures

A trader buys 1 WTI crude oil futures contract at $75 per barrel.

Later, the trader exits the position at $80 per barrel.

### Inputs

| Input | Value |
|---|---:|
| Position | Long |
| Entry price | $75/bbl |
| Exit price | $80/bbl |
| Contract size | 1,000 barrels |
| Number of contracts | 1 |

### Calculation

Price move:

$80 - $75 = +$5 per barrel

P&L:

+$5 × 1,000 barrels × 1 contract = +$5,000

### Expected Output

The trader made a profit of $5,000.

### Trading Intuition

A long futures position gains when the futures price rises.

The trader bought at $75 and exited at $80, so they benefited from the $5 price increase.

## Example 2: Short WTI Futures

A trader sells 1 WTI crude oil futures contract at $75 per barrel.

Later, the trader exits the position at $70 per barrel.

### Inputs

| Input | Value |
|---|---:|
| Position | Short |
| Entry price | $75/bbl |
| Exit price | $70/bbl |
| Contract size | 1,000 barrels |
| Number of contracts | 1 |

### Calculation

Price move:

$70 - $75 = -$5 per barrel

P&L:

+$5 × 1,000 barrels × 1 contract = +$5,000

### Expected Output

The trader made a profit of $5,000.

### Trading Intuition

A short futures position gains when the futures price falls.

The trader sold at $75 and exited at $70, so they benefited from the $5 price decrease.

## Key Takeaways

- Long futures gain when prices rise.
- Short futures gain when prices fall.
- Contract size turns a small price move into a larger dollar P&L.
- For WTI crude, a $1 move equals $1,000 per contract because the contract size is 1,000 barrels.