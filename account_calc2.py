#
# account_calc.py
#
# A program to determine the change in a person's savings account
# as the result of a series of transactions.
#
# author: Computer Science 105, Boston University
# modified by: <PUT YOUR NAME HERE>
# 

start = int(input('Enter the starting balance: '))
num_trans = int(input('Enter the number of transactions: '))
change = 0
    
for i in range(num_trans):
    amount = int(input('Enter a deposit or withdrawal amount: '))
    change += amount
    print()

perc_change = (100 * change) / start
new_bal = start + change
print('After', num_trans, 'transactions, the new account balance is', new_bal, 'dollars.')
print('The percent change in the account is', perc_change, 'percent.')
