# Create class User with proper methods:
#         get_account_balance(),  change_password()
#         Create decorator to handle errors, listed below

def excep(func):
    def wrapper(*args, **kwargs):
        if ValueError:
            raise Exception
        else:
            return func(*args, **kwargs)
        # try:
        #     return func(*args, **kwargs)
        # except Exception as e:
        #     if ValueError:
            # raise
        # except TypeError as e:
        #     print('Error occured', e)
        # except TypeError as e:
        #     print('Error occured ', e)
    return wrapper

class User: 
    def __init__(self,name): 
        self.name = name
        self.balance=0
        print("Hello Noka!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("You Withdrew:", amount) 
        else: 
            print("Insufficient balance  ") 

    @excep
    def get_account_balance(self): 
        print("Your Available Balance=",self.balance) 

    @excep
    def change_password(self):
        self.password = []
        self.password = float(input("Enter new password: "))
        print("\n Your password been changed ") 


u = User('Noka') 
u.deposit() 
u.withdraw()
u.get_account_balance()
u.change_password() 
