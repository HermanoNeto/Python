account_number = input('Enter account number: ')
account_holder = input('Enter account holder: ')
inicial_verify = input('Is there an initial deposit (y/n)? ')

account = 0

if inicial_verify.lower() == 'y':
    inicial_deposit = int(input('Enter initial deposit value: '))
    account += inicial_deposit

print(f'Account data:\nAccount {account_number}, Holder: {account_holder}, Balance: ${float(account)}')

deposit = int(input('Enter a deposit value: '))
account += deposit

print(f'Updated account data:\nAccount {account_number}, Holder: {account_holder}, Balance: ${float(account)}')

withdraw = int(input('Enter a withdraw value: '))
account -= withdraw

print(f'Updated account data:\nAccount {account_number}, Holder: {account_holder}, Balance: ${float(account)}')