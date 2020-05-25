import datetime

open_transactions = []

def timestamp():
    # Function that will return current date and time
    current = datetime.datetime.now()
    change2string = str(current)
    return change2string

def add_transaction (sender, recipient, amount=1, timestamp=timestamp):
    # Append a new value as well as well as the last blockchain value to the blockchain
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount, 'timestamp': timestamp}
    open_transactions.append(transaction)
   
def get_transaction_value():
    #Returns the input of the user(a new transaction amount)
    bc_sender = str(input('Please enter name of sender: '))
    bc_recipient = str(input('Please enter of recipient: '))
    bc_amount = float(input('Please enter the amount: '))
    bc_timestamp = timestamp()
    return (bc_sender, bc_recipient, bc_amount, bc_timestamp)

def get_user_choice():
    # Prompts the user to make a choice and return it
    user_input = input('Make a choice: ')
    return user_input







while True:
    print('Welcome to the transaction recording program')
    print('-' * 45)
    print('Please choose from the following options:')
    print("Type 'yes' to add a new transaction")
    print('Press q to quit')

    user_choice = get_user_choice()
    if user_choice == 'yes':
        tx_data = get_transaction_value()
        sender, recipient, amount, timestamp = tx_data
      # add the transaction amount to the blockchain
        add_transaction(sender, recipient, amount, timestamp)
        print(open_transactions)
    elif user_choice == 'q':
      # This will end the loop
        break
    else:
        print ('Invalid input, please choose a value from list!\n')

print('You have successfully logged out!')