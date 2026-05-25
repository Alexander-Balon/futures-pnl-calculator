from contracts import PotentialContracts
from helpers import shortPnl
from helpers import longPnl

hedging_mode = int(input("Please enter 1 to examine a calendar spread, 2 to examine a time spread, and 3 to examine a crack spread: "))

while hedging_mode not in [1, 2, 3]:
    hedging_mode = int(input("Please enter 1 to examine a calendar spread, 2 to examine a time spread, and 3 to examine a crack spread: "))

if hedging_mode == 1: 
    selected_contract = input(
        '''Please provide your contract for the calendar spread ("wti", "brent", "henry_hub", "rbob", "ulsd"): '''
    ).strip().lower()

    #Uses the contract type to add standard specifications
    contract_info = PotentialContracts[selected_contract]

    contract_elements = {
    "Contract Name": contract_info["name"],
    "Contract Size": contract_info["contract_size"],
    "Unit": contract_info["unit"],
    "Contract Position": "",
    "Entry Price": 0,
    "Exit Price": 0,
    "Number of Contracts": 0
    }

    user_inputs = ["Contract Position", "Entry Price", "Exit Price", "Number of Contracts"]

    current_leg = 0
    pnls, contract_positions = [0, 0], ["",""]
    entry_prices, exit_prices = [0, 0], [0, 0]

    while current_leg < 2: 
        print(f"Please fill in information for the {"first" if current_leg == 0 else "second"} leg") 
        print("-"*30)
        for contract_element in user_inputs:
            if contract_element == "Contract Position": 
                contract_elements["Contract Position"] =  input(f"Please enter the {contract_element.lower()}: ").strip().lower()
                contract_positions[current_leg] = contract_elements["Contract Position"]
            else:
                contract_elements[contract_element] = float(input(f"Please enter the {contract_element.lower()}: "))
                if contract_element == "Entry Price":
                    entry_prices[current_leg] = contract_elements["Entry Price"]
                if contract_element == "Exit Price":
                    entry_prices[current_leg] = contract_elements["Exit Price"]
            if contract_elements["Contract Position"] == "long" and contract_elements["Number of Contracts"] != 0:
                pnls[current_leg] = longPnl(contract_elements["Entry Price"],contract_elements["Exit Price"],contract_elements["Contract Size"],contract_elements["Number of Contracts"])
            elif contract_elements["Number of Contracts"] != 0:
                pnls[current_leg] = shortPnl(contract_elements["Entry Price"],contract_elements["Exit Price"],contract_elements["Contract Size"],contract_elements["Number of Contracts"])
        current_leg +=1 

    final_pnl = pnls[0] + pnls[1]
    initial_spread_value = entry_prices[0] - entry_prices[1]
    final_spread_value = exit_prices[0] - exit_prices[1]

    if contract_positions[0] == "long":
        print("You were long the calendar spread. You stood to benefit if the spread value increased (the first leg becomes stronger relative to the second leg)")
        if final_spread_value > initial_spread_value:
             print(f"Because the spread value increased, you made a proft. Your profit was: ${final_pnl}.")
        elif initial_spread_value < final_spread_value: 
             print(f"Because the spread decreased, you did not made a proft. Your loss was: ${final_pnl}.")
        else:
             print("The spread did not change. You did not incur a profit or a loss.")

    if contract_positions[0] == "short":
        print("You were short the calendar spread. You stood to benefit if the spread value decreased (the second leg became stronger relative to the first leg)")
        if final_spread_value > initial_spread_value:
             print(f"Because the spread value increased, you did not make a profit. Your loss  was: ${final_pnl}.")
        elif initial_spread_value < final_spread_value: 
             print(f"Because the spread decreased, you made a proft. Your profit was: ${final_pnl}.")
        else:
             print("The spread did not change. You did not incur a profit or a loss.")