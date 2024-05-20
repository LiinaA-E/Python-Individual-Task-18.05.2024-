# Python-Individual-Task-18.05.2024-
### Easy Level
**Description:**
Create a program where the user can input deposits into a bank account. The program should use `if-else` statements, `input()`, `int()` and while True loop to keep track of deposits.

**Instructions:**
1. Welcome the user to the bank
2. Initiate balance = 0
3. Ask the user to input the amount of money they want to deposit.
4. Add the deposit amount to the total balance
5. Ask the user if they want to make another deposit or exit the bank. 
6. If they choose to make another deposit, repeat the process (while True).
7. If not, print the total amount deposited and exit the bank.

### Medium Level
**Instructions:**
1. Use `try` and `except` to handle non-integer inputs for deposits.

```py
print ('Welcome to the bank')
balance = 0

while True:
  try:
    deposit = int (input('Please input the amount of money, you wish to deposit: '))
    balance = balance + deposit
    option = input('To make another deposit click enter, to exit the bank, write "EXIT" ').upper()
    if option == 'EXIT':
      print(f'Total amount deposited are {balance}.')
      break
    else:
      continue
  except Exception as e:
    print(f'Wrong input, exeption: {e}, please provide only numbers')
    continue    
print('You are now exiting the bank')
```

### Hard Level
**Instructions:**
1. Add bank withdrawal (if user wants to withdraw money the balance decreases)
2. If the balance becomes negative, withdrawal is not possible.
3. Add check balance optionality
Example for hard level:
   print("\nWhat would you like to do?")
   print("1. Deposit money")
   print("2. Withdraw money")
   print("3. Check balance")
   print("4. Exit")

```py
print ('Welcome to the bank')
balance = 0

def check_balance(balance):
  balance
  print(f'Your current balance is {balance}')

while True:
  print('Enter "1"- to deposit money.')
  print('Enter "2" - to withdraw money.')
  print('Enter "3" - to check balance.')
  print('Enter "4" - to EXIT.')
  try:
    option = int (input('What would you like to do? '))

    if option == 4:
      break

    elif option == 1:
      while True:
        try:
          deposit = int (input('Please input the amount of money, you wish to deposit: '))
          balance = (balance + deposit)
          print('Funds have been successfully deposited into your account!')
          check_balance(balance)
          break
        except Exception as e:
          print(f'Wrong input, exeption: {e}, please provide only numbers.')
          continue
      
    elif option == 2:
      while True:
        try:
          withdraw = int (input('Please input the amount of money, you wish to withdraw: '))
          if (balance - withdraw < 0):
           print('There are insufficient funds in the account, withdrawal is not possible.')
           break
          else:
           balance = (balance - withdraw)
           print('Withdrawal was successful.')
           check_balance(balance)
           break
        except Exception as e:
          print(f'Wrong input, exeption: {e}, please provide only numbers.')
          continue
      
    elif option == 3:
      check_balance(balance)

    else:
      print('Please provide only number "1", "2", "3", or "4".')
      continue

  except Exception as e:
    print(f'Wrong input, exeption: {e}, please provide only numbers.')
    continue

print('You are now exiting the bank.')
```
