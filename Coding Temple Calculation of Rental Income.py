from tabulate import tabulate
import os

incomes = {
    "--------INCOME--------": "##############",
    "Rental Income": 0.00,
    "Laundry Income": 0.00,
    "Storage Income": 0.00,
    "Misc Income": 0.00,
    "Total Monthly Income": 0.00
}

expenses = {
    "------EXPENSES------": "##############",
    "Taxes" : 0.00,
    "Insurance": 0.00,
    "Water/Sewer": 0.00,
    "Garbage": 0.00,
    "Electric/Gas": 0.00,
    "HOA Fee": 0.00,
    "Lawn/Snow": 0.00,
    "Vacancy": 0.00,
    "Repairs": 0.00,
    "CapEx": 0.00,
    "Prop. Mgmt": 0.00,
    "Mortgage": 0.00,
    "Total Monthly Expenses": 0.00
}

cashflow = {
    "------CASHFLOW------": "##############",
    "Total Monthly Income": 0.00,
    "Total Monthly Expenses": 0.00,
    "Total Monthly Cashflow": 0.00,
    "Total Annual Cashflow": 0.00
}

cashoncash = {
    "--Cash on Cash Return-": "##############",
    "Down Payment" : 0.00,
    "Closing Costs" : 0.00,
    "Rehab Budget" : 0.00,
    "Misc Other" : 0.00,
    "Total Investment" : 0.00,
    "Cash on Cash Return*": 0.00
}

def matchAmounts():
    incomes["Total Monthly Income"] = 0.00
    for r,p in incomes.items():
        if r != "Total Monthly Income" and r != "--------INCOME--------":
            incomes["Total Monthly Income"] += p

    expenses["Total Monthly Expenses"] = 0.00
    for t,v in expenses.items():
        if t != "Total Monthly Expenses" and t != "------EXPENSES------":
            expenses["Total Monthly Expenses"] += v

    cashoncash["Total Investment"] = 0.00
    for i, k in cashoncash.items():
        if i != "--Cash on Cash Return-" and i !="Cash on Cash Return" and i !="Total Investment":
            cashoncash["Total Investment"] += k

    cashflow["Total Monthly Income"] = incomes["Total Monthly Income"]
    cashflow["Total Monthly Expenses"] = expenses["Total Monthly Expenses"]
    cashflow["Total Monthly Cashflow"] = cashflow["Total Monthly Income"] - expenses["Total Monthly Expenses"]
    cashflow["Total Annual Cashflow"] = cashflow["Total Monthly Cashflow"] * 12

    try:
        cashoncash["Cash on Cash Return"] = cashflow["Total Annual Cashflow"] / cashoncash["Total Investment"] * 100
        cashoncash["Cash on Cash Return"] = int(cashoncash["Cash on Cash Return"])
    except:
        cashoncash["Cash on Cash Return"] = 0.00

IncomeHeader = ["Category", "Costs"]

def printLists():
    os.system('cls')
    print("\n")
    print("Welcome to our Rental Property Calculator!")
    print("\n")
    print(tabulate(incomes.items(), headers=IncomeHeader, tablefmt="grid"))
    print(tabulate(expenses.items(), headers=IncomeHeader, tablefmt="grid"))
    print(tabulate(cashflow.items(), headers=IncomeHeader, tablefmt="grid"))
    print(tabulate(cashoncash.items(), headers=IncomeHeader, tablefmt="grid"))
    print("*Cash on Cash Return amount is a percentage. Add a percent sign to the number." + "\n")

quitprogram = False
while quitprogram == False:
    os.system('cls')
    printLists()
    print("Select a Number from the list below:")
    print("1) Income")
    print("2) Expenses")
    print("3) Cashflow")
    print("4) Cash on Cash Return")
    print("5) Quit Program")
    choice = int(input("Choice: "))
    if choice:
        if choice == 5:
            quitprogram = True
        else:
            category = input("Copy and paste the category you would like to add a price to: ")
            category = category.rstrip(' ')
            category = category.lstrip(' ')
            catvalue = float(input("Enter the new value: "))
            if choice == 1:
                incomes[category] = catvalue
            elif choice == 2:
                expenses[category] = catvalue
            elif choice == 3:
                cashflow[category] = catvalue
            elif choice == 4:
                cashoncash[category] = catvalue
            matchAmounts()