import re, random

class bank_system:
    def __init__(self, balance,password):
        self.balance = balance
        self.password = password
        self.account_list= {}
    def ask_balance (self):
        print(f"Your balance is {self.balance}")
        return True
    def create_account(self):
        name = input("Enter your name: ").strip()
        phone = input("Enter your phone number: ").strip()
        if not re.match(r"^09[0-9]{8}$",phone):
            print("Invalid number! ")
            return False
        adress = input("Enter your adress: ")
        birthdate = input("Enter your birth date: ")
        if not re.match(r"^(3[0-1]|[0-2][0-9]).+(-).+(1[0-2]|[0-9]).+(-).+([0-2][0-9]{3})"):
            print("Enter a valid date!")
            return False
        password = input("Enter your password: ")
        account_number= "1000" + str((random.randint(100000000,999999999)))
    
        if  account_number not in self.account_list:
            self.account_list[account_number]= True
        else:
            print("The account number has been used.")
            
        print ("\n\nCongratulation! you have successfully create your account. ")
        print (f"your account information is as following ")
        print(f"\n Name = {name} \n your phone number is {phone} \n your adress {adress} \n birthdate {birthdate} \n your password is {password} .")
        print (f"\n Your account number is {account_number}")
    def withdraw(self):
        password = input("Enter your password: ")
        if password == self.password:
            
            try:
                amount = int(input("Enter the amount you want to withdraw: "))
            except ValueError:
                print("invalid amount! ")
                return False
            if self.balance >= amount:
                self.balance -= amount
                print (f"You have withdrawn {amount} from your account.")
                print(f"YOur balance is now {self.balance}")
                return True
            else:
                print(f"Insufficient balance! please enter your amount in the range of 0-{self.balance}")
                return False
            
    def transfer_other_account(self):
        receiver_account = input("Please enter the receiver's account number: ")
    
        if not re.match(r"^1000[0-9]{9}$", receiver_account):
            print("The account you entered is not in our bank!")
            return False
        
        try:
            amount = int(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount!")
            return False

        
        if self.balance >= amount:
            self.balance -= amount
            print(f"Transfer of {amount} to account {receiver_account} is successful.")
            print(f"You have left with {self.balance}")
            return True
        else:
            print("Insufficient balance in your account.")
            return False
    def Top_up(self):
        phone = input("Enter your phone number: ").strip()
        if not re.match(r"^09[0-9]{8}$",phone):
            print("Invalid number! ")
            return False
        
        else:
            password = input("password: ")
            if password == self.password:
                amount = int(input("amount: "))
                if amount > 0 and amount % 5 == 0:
                    self.balance -= amount
                    confirmation_password = input("Enter your confirmation_password: ")
                    if confirmation_password == self.password:
                        print("You have successfully withdrawn money.")
                        print(f"your balance is {self.balance}birr.")
                    else:
                        print("The confirmation password didn't match with password.")
                else:
                    print("card must be 5 and its multiplication!")
            else:
                print("Somthing wrong with password check it again!")
                
if __name__ =='__main__':
    berihun = bank_system(5000, 'liyu12345')

    while True :
        print("****************WELCOME TO OUR BANK*******************\n")
        print("What do you want to do?")
        print("Transaction Types are here ")
        print("1. Create account ")
        print("2. Ask balance ")
        print("3. With draw ")
        print("4. Transfer to other account ")
        print("5. Top Up")
        userchoice = int(input("Enter the choice you want to excute: "))
        
        if userchoice == 1:
            berihun.create_account()
        elif userchoice == 2:
            berihun.ask_balance()
        elif userchoice == 3:
            berihun.withdraw()
        elif userchoice == 4:
            berihun.transfer_other_account()
        elif userchoice == 5:
            berihun.Top_up()
        
        
        print ("\n\nWould you like to do some other Transactions? ")
        userchoice2 = input("\nPlease  c to continue or any other key  to quit: ")
        if userchoice2 == 'c':
            continue
        else:
            break    