# Natural Gas Futures P&L Example

## Purpose

This example shows how Henry Hub natural gas futures P&L works.

Natural gas futures are useful because even small price changes can create meaningful dollar gains or losses due to the large contract size.

## Contract

| Item | Value |
|---|---:|
| Contract | Henry Hub Natural Gas Futures |
| Unit | MMBtu |
| Contract size | 10,000 MMBtu |
| Price unit | Dollars per MMBtu |

## Example 1: Long Henry Hub Futures

A trader buys 1 Henry Hub natural gas futures contract at $3.20/MMBtu.

Later, the trader exits the position at $3.45/MMBtu.

### Inputs

| Input | Value |
|---|---:|
| Position | Long |
| Entry price | $3.20/MMBtu |
| Exit price | $3.45/MMBtu |
| Contract size | 10,000 MMBtu |
| Number of contracts | 1 |

### Calculation

Price move:

$3.45 - $3.20 = +$0.25/MMBtu

P&L:

+$0.25 × 10,000 MMBtu × 1 contract = +$2,500

### Expected Output

The trader made a profit of $2,500.

### Trading Intuition

A long natural gas futures position gains when natural gas prices rise.

Even though the price only increased by $0.25, the contract size is 10,000 MMBtu, so the dollar gain is meaningful.

## Example 2: Short Henry Hub Futures

A trader sells 2 Henry Hub natural gas futures contracts at $3.20/MMBtu.

Later, the trader exits the position at $3.00/MMBtu.

### Inputs

| Input | Value |
|---|---:|
| Position | Short |
| Entry price | $3.20/MMBtu |
| Exit price | $3.00/MMBtu |
| Contract size | 10,000 MMBtu |
| Number of contracts | 2 |

### Calculation

Price move:

$3.00 - $3.20 = -$0.20/MMBtu

P&L:

+$0.20 × 10,000 MMBtu × 2 contracts = +$4,000

### Expected Output

The trader made a profit of $4,000.

### Trading Intuition

A short futures position gains when prices fall.

The trader was short 2 contracts, so the gain is doubled compared with a 1-contract position.

## Key Takeaways

- Henry Hub futures are priced in dollars per MMBtu.
- One Henry Hub futures contract represents 10,000 MMBtu.
- A $0.01 move equals $100 per contract.
- Long natural gas futures gain when prices rise.
- Short natural gas futures gain when prices fall.