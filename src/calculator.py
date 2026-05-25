from helpers import shortPnl
from helpers import longPnl
from contracts import PotentialContracts


# Ask user to select a contract
selected_contract = input(
    '''Please provide your contract ("wti", "brent", "henry_hub", "rbob", "ulsd"): '''
).strip().lower()


# Validate selected contract
while selected_contract not in PotentialContracts:
    print ("-" * 30)
    print("Key Table")
    print("-" * 15)
    for contract in PotentialContracts:
        print(contract + ": " + PotentialContracts[contract]["name"])
    print ("-" * 30)
    selected_contract = input(
        '''Invalid contract. Please refer to the key and enter "wti", "brent", "henry_hub", "rbob", or "ulsd": '''
    ).strip().lower()


# Pull preset contract information from contracts.py
contract_info = PotentialContracts[selected_contract]


# Start the trade dictionary with preset contract details
contract_elements = {
    "Contract Name": contract_info["name"],
    "Contract Size": contract_info["contract_size"],
    "Unit": contract_info["unit"],
    "Contract Position": "",
    "Entry Price": 0,
    "Exit Price": 0,
    "Number of Contracts": 0
}


# Ask only for the trade-specific information
user_inputs = ["Contract Position", "Entry Price", "Exit Price", "Number of Contracts"]

for contract_element in user_inputs:
    if contract_element == "Contract Position":
        contract_elements[contract_element] = input(
            f"Please enter the {contract_element.lower()}: "
        ).strip().lower()
    else:
        while True:
            try:
                contract_elements[contract_element] = float(
                    input(f"Please enter the {contract_element.lower()}: ")
                )
                break
            except ValueError:
                print("Please enter a number with no spaces or commas between digits.")


# Validate long/short position
while contract_elements["Contract Position"] not in ["long", "short"]:
    contract_elements["Contract Position"] = input(
        '''Please enter either "long" or "short" as the contract position: '''
    ).strip().lower()


# Calculate P&L
if contract_elements["Contract Position"] == "long":
    pnl = longPnl(
        contract_elements["Entry Price"],
        contract_elements["Exit Price"],
        contract_elements["Contract Size"],
        contract_elements["Number of Contracts"]
    )
else:
    pnl = shortPnl(
        contract_elements["Entry Price"],
        contract_elements["Exit Price"],
        contract_elements["Contract Size"],
        contract_elements["Number of Contracts"]
    )


# Calculate price move
price_move = contract_elements["Exit Price"] - contract_elements["Entry Price"]

if price_move > 0:
    price_move_display = "+$" + str(abs(price_move))
elif price_move < 0:
    price_move_display = "-$" + str(abs(price_move))
else:
    price_move_display = "$0"


# Format P&L
if pnl > 0:
    pnl_display = "+$" + str(abs(pnl))
elif pnl < 0:
    pnl_display = "-$" + str(abs(pnl))
else:
    pnl_display = "$0"


# Print output
print("-" * 30)

print(
    "You were "
    + contract_elements["Contract Position"]
    + " "
    + str(contract_elements["Number of Contracts"])
    + " "
    + contract_elements["Contract Name"]
    + " futures contract(s)."
)

print(
    "Entry Price: $" + str(contract_elements["Entry Price"]) + "\n"
    + "Exit Price: $" + str(contract_elements["Exit Price"]) + "\n"
    + "Price Move: " + price_move_display + "\n"
    + "Contract Size: " + str(contract_elements["Contract Size"]) + " "
    + contract_elements["Unit"] + "\n"
    + "Number of Contracts: " + str(contract_elements["Number of Contracts"])
)

if contract_elements["Contract Position"] == "long":
    if price_move > 0:
        print("Because you were long, you benefited from the price increase.")
    elif price_move < 0:
        print("Because you were long, you were hurt by the price decrease.")
    else:
        print("Because the price did not move, your futures P&L was zero.")

if contract_elements["Contract Position"] == "short":
    if price_move < 0:
        print("Because you were short, you benefited from the price decrease.")
    elif price_move > 0:
        print("Because you were short, you were hurt by the price increase.")
    else:
        print("Because the price did not move, your futures P&L was zero.")

print("Total P&L: " + pnl_display)

print("-" * 30)