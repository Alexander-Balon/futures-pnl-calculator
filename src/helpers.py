def shortPnl(entry_price, exit_price, contracts, number_of_contracts):
    return round((entry_price - exit_price) * (contracts * number_of_contracts), 2)

def longPnl(entry_price, exit_price, contracts, contract_multiplier): 
    return round((exit_price - entry_price) * (contracts * contract_multiplier), 2)