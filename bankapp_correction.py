import random
import time
from datetime import datetime

data = {}

def deposit(amount:float, prev_bal:float):
    """This function provides the logic for depositing money into an account.

    Args:
        amount (float): The amount to be deposited.
        prev_bal (float): The former amount available

    Returns:
        new_bal (float) : The new balance after deposit.
    """
    new_bal = amount+prev_bal
    return new_bal



def withdraw(amount:float, prev_bal:float):
    """This function provides the logic for depositing money into an account.

    Args:
        amount (float): The amount to be withdrawn.
        prev_bal (float): The former amount available.

    Returns:
        new_bal (float) : The new balance after withdrawal.
    """
    if amount > prev_bal:
        raise ValueError("Insuffucient funds")
    else:
        new_bal = prev_bal-amount
        return new_bal


def account_num():
    val = "0"
    for _ in range(9):
        val+=str(random.choice(range(10)))
        
    return val


print("Welcome to the Bitcoin Core")
while True:
    print("What would you like to do?\n1. Create a new account.\n2. Login to an existing account.\n3. Quit.")
    user_input = input('::>>')

    if user_input == '1':
        #take the credentials for account creation
        f_name = input('First Name:\n>') 
        l_name = input('Last Name:\n>')
        pin = input('Login Pin:\n>')
        trans_pin = input('Transaction Pin:\n>')
        acc_num = account_num()
        print("Account creation processing...")
        time.sleep(3)
        print('Successful')
        time.sleep(2)
        
        #create a new key value pair for the account in the dictionary. 
        data[acc_num] = {
            'name' : f"{f_name} {l_name}",
            'pin' : pin,
            'trans_pin' : trans_pin,
            'bal' :0,
        }
        
        #print success message
        print(f"""\nWelcome, {f_name}!
You have successfully created your account on the bitcoin core. Your account number is {acc_num}.
Please keep your pin safe from scammers.          
Cheers,
CoachE.
(CEO Bitcoin Core)""")
        
    elif user_input == "2":
        #take in login information from the user.
        acc_num = input('Account Number:\n>')
        pin = input('Login Pin:\n>')
        
        #verify that the user exists in the dictionary.
        user_data = data.get(acc_num)
        
        #check that the user data does not return none and that the pin is correct.
        if user_data and user_data.get("pin") == pin:
            print("Login Successful")
            first_login = True #set the first login value to True
            while True:
                if first_login:
                    print(f"Welcome, {user_data['name'].split()[0].title()}")
                    first_login = False #set the value to false to give proper welcome back message.
                else:
                    print(f"Welcome back, {user_data['name'].split()[0].capitalize()}")
                
                print("What would you like to do?\n1. Withdraw.\n2. Deposit.\n3. Transfer.\n4. Check Balance\n5. Logout")
                input_ = input(":>>")
                if input_ == "1":
                    amount = float(input("Amount:\n>"))
                    
                    try:
                        new_bal = withdraw(amount, user_data['bal']
                                )
                        user_data['bal'] = new_bal
                    except ValueError as msg:
                        print(msg)
                elif input_ == "2":
                    amount = float(input("Amount:\n>"))
                    trans_pin = input("Transaction Pin:\n>")
                    if trans_pin == user_data['trans_pin']:
                        amt = deposit(amount, user_data['bal'])
                        user_data['bal'] = amt
                    else:
                        print("Invalid pin value")
                elif input_ == '3':
                    other_acc = input("Enter Account number\n:>> ")
                    trans_amount = int(input("Enter Amount you want to Transfer\n:>> "))
                    trans_pin = input("Enter transaction pin:\n>")
                  
                    beneficiary = data.get(other_acc) #get the beneficiary detail.
                #   print(beneficiary)
                    if beneficiary:
                        if trans_amount > user_data['bal']:
                            print("Insufficient Funds")
                        else:   
                            if trans_pin == user_data['trans_pin']:
                                user_data['bal'] -= trans_amount #take money out of the sender's aza
                      
                                beneficiary['bal'] += trans_amount #put the money into the receiver's acc.
                      
                                print("\nTransfer Successful")
                            else:
                                print("Incorrect pin.")
                elif input_ == '4':
                    current_date = datetime.now().date()
                    date = current_date.strftime("%a, %d of %B, %Y")
                    print(f"Your current balance at {date} is {user_data['bal']}")
                    
                elif input_ == "5":
                    break        
                    
        else:
            print("Invalid credentials.")
    elif user_input == "3":
        break
    
print('\n', data)





