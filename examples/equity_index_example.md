# Equity Index Futures P&L Example

## Purpose

This example shows how futures P&L can also apply outside commodities.

The same long/short logic works for equity index futures, but the contract size is based on an index multiplier instead of barrels, gallons, or MMBtu.

## Contract

| Item | Value |
|---|---:|
| Contract | Equity Index Future |
| Unit | Index points |
| Multiplier | $50 per index point |
| Price unit | Index points |

## Example 1: Long Equity Index Futures

A trader buys 1 equity index futures contract at 5,000.

Later, the trader exits the position at 5,050.

### Inputs

| Input | Value |
|---|---:|
| Position | Long |
| Entry price | 5,000 |
| Exit price | 5,050 |
| Multiplier | $50 per point |
| Number of contracts | 1 |

### Calculation

Price move:

5,050 - 5,000 = +50 points

P&L:

+50 points × $50 × 1 contract = +$2,500

### Expected Output

The trader made a profit of $2,500.

### Trading Intuition

A long futures position gains when the index rises.

The trader bought exposure to the index at 5,000 and exited at 5,050.

## Example 2: Short Equity Index Futures

A trader sells 1 equity index futures contract at 5,000.

Later, the trader exits the position at 4,940.

### Inputs

| Input | Value |
|---|---:|
| Position | Short |
| Entry price | 5,000 |
| Exit price | 4,940 |
| Multiplier | $50 per point |
| Number of contracts | 1 |

### Calculation

Price move:

4,940 - 5,000 = -60 points

P&L:

+60 points × $50 × 1 contract = +$3,000

### Expected Output

The trader made a profit of $3,000.

### Trading Intuition

A short futures position gains when the index falls.

The trader sold exposure at 5,000 and exited at 4,940.

## Key Takeaways

- The same futures P&L logic applies across asset classes.
- Long futures gain when the price rises.
- Short futures gain when the price falls.
- For equity index futures, the contract size is usually represented by a dollar multiplier per index point.
- A larger multiplier creates larger dollar P&L for the same point move.