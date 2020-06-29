#Program that allows a user to access two different financial calculators: 
#an investment calculator and a home loan repayment calculator

import sys
import math

#Determine type of calculator the user requires

print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("\nInvestment\t - to calculate the amount of interest you'll earn on interest")
print("Bond\t\t - to calculate the amount you'll have to pay on a home loan")
print()
calculator = input()

#Match calculation and requirements via if-elif-else statement

if (calculator.lower() == "investment") :
    
    #Get required variables from user
    
    deposit = float(input("How mamy Rands are you depositing?\nR"))
    interest = float(input("What percentage interest are you earning?\n"))
    
    #Convert given interest value to a percentage
    
    interest /= 100
    
    #choice of declaring investment period as months or years and converting to calculation required years if needed 
    
    time_unit = input("Would you like to indicate investment period as 'years' or 'months'?\n")
    
    if (time_unit.lower() == "years") :
        time = float(input("Over how many years would you like to invest?\n"))
    
    elif (time_unit.lower() == "months") :
        time = float(input("Over how many months would you like to invest?\n"))
        time /= 12
    
    else :
        sys.exit("Your input matches neither 'years' or 'months'.")
    
    #choice of compound or simple interest calculation
    
    interest_type = input("Will your investment be calculated using 'simple' or 'compound' interest?\n")
    
    if (interest_type.lower() != "simple" and interest_type.lower() != "compound") :
        sys.exit("Your input matches neither 'simple' or 'compound'.")
    
    #Calculate expected end value of investment
    
    if (interest_type.lower() == "simple") :
        final_value = deposit * (1 + interest * time)
    
    else :
        final_value = deposit * math.pow((1 + interest), time)
    
    print(f"\nThe expected final value on your investment of R{deposit:.2f}, calculated over {time:.2f} years and at {interest * 100:.2f}%, is:\nR{final_value:.2f}")

elif (calculator.lower() == "bond") :
    
    #Get required variables from user
    
    house_value = float(input("How mamy Rands is your house worth?\nR"))
    interest = float(input("What percentage interest are you being charged?\n"))
    
    #Convert given interest value to a percentage
    
    interest /= 100
    
    #choice of declaring repayment period as months or years and converting to calculation required months if needed 
    
    time_unit = input("Would you like to indicate your repayment period as 'years' or 'months'?\n")
    
    if (time_unit.lower() == "years") :
        time = float(input("Over how many years would you like to repay your bond?\n"))
        time *= 12
    
    elif (time_unit.lower() == "months") :
        time = float(input("Over how many months would you like to repay your bond?\n"))
    
    else :
        sys.exit("Your input matches neither 'years' or 'months'.")
    
    #Calculate expected monthly installment
    
    monthly_installment = ((interest / 12) * house_value) / (1 - math.pow(1 + (interest / 12), -time))
    
    print(f"Your monthly bond repayment on a R{house_value:.2f} house, over the course of {time: .0f} months, is\nR{monthly_installment}")
 
else :
    sys.exit("Your input matches neither 'investment' or 'bond'.")
