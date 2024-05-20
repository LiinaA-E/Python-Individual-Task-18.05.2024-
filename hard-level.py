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
