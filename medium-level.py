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
