import re
import random
import bcrypt # type: ignore

class BankSystem:
    def __init__(self, balance, password):
        self.balance = balance
        self.password = self.hash_password(password)
        self.account_list = {}

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def ask_balance(self):
        print(f"Your balance is {self.balance}")
        return True

    def create_account(self):
        name = input("Enter your name: ").strip()
        phone = input("Enter your phone number: ").strip()
        if not re.match(r"^09[0-9]{8}$", phone):
            print("Invalid number!")
            return False
        address = input("Enter your address: ")
        birthdate = input("Enter your birth date (DD-MM-YYYY): ")
        if not re.match(r"^(3[0-1]|[0-2][0-9])-(1[0-2]|0[1-9])-([0-2][0-9]{3})$", birthdate):
            print("Enter a valid date!")
            return False
        password = input("Enter your password: ")
        hashed_password = self.hash_password(password)
        account_number = "1000" + str(random.randint(100000000, 999999999))

        if account_number not in self.account_list:
            self.account_list[account_number] = {
                "name": name,
                "phone": phone,
                "address": address,
                "birthdate": birthdate,
                "password": hashed_password,
                "balance": 0
            }
        else:
            print("The account number has been used.")
            return False

        print("\n\nCongratulations! You have successfully created your account.")
        print(f"Your account information is as follows:")
        print(f"\n Name = {name} \n Phone number = {phone} \n Address = {address} \n Birthdate = {birthdate} \n Password = {password}.")
        print(f"\n Your account number is {account_number}")
        return True

    def withdraw(self):
        password = input("Enter your password: ")
        if self.check_password(password):
            try:
                amount = int(input("Enter the amount you want to withdraw: "))
            except ValueError:
                print("Invalid amount!")
                return False
            if self.balance >= amount:
                self.balance -= amount
                print(f"You have withdrawn {amount} from your account.")
                print(f"Your balance is now {self.balance}")
                return True
            else:
                print(f"Insufficient balance! Please enter an amount in the range of 0-{self.balance}")
                return False
        else:
            print("Incorrect password!")
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
            print(f"You have {self.balance} left in your account.")
            return True
        else:
            print("Insufficient balance in your account.")
            return False

    def top_up(self):
        phone = input("Enter your phone number: ").strip()
        if not re.match(r"^09[0-9]{8}$", phone):
            print("Invalid number!")
            return False

        password = input("Enter your password: ")
        if self.check_password(password):
            try:
                amount = int(input("Enter the amount: "))
            except ValueError:
                print("Invalid amount!")
                return False
            if amount > 0 and amount % 5 == 0:
                self.balance -= amount
                confirmation_password = input("Enter your confirmation password: ")
                if self.check_password(confirmation_password):
                    print("You have successfully withdrawn money.")
                    print(f"Your balance is {self.balance} birr.")
                else:
                    print("The confirmation password didn't match the password.")
            else:
                print("Amount must be a multiple of 5!")
        else:
            print("Incorrect password!")
            return False

if __name__ == '__main__':
    berihun = BankSystem(5000, 'liyu12345')

    while True:
        print("****************WELCOME TO OUR BANK*******************\n")
        print("What do you want to do?")
        print("Transaction Types are here:")
        print("1. Create account")
        print("2. Ask balance")
        print("3. Withdraw")
        print("4. Transfer to other account")
        print("5. Top Up")
        try:
            userchoice = int(input("Enter the choice you want to execute: "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        if userchoice == 1:
            berihun.create_account()
        elif userchoice == 2:
            berihun.ask_balance()
        elif userchoice == 3:
            berihun.withdraw()
        elif userchoice == 4:
            berihun.transfer_other_account()
        elif userchoice == 5:
            berihun.top_up()
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

        print("\n\nWould you like to do some other transactions?")
        userchoice2 = input("\nPlease enter 'c' to continue or any other key to quit: ")
        if userchoice2.lower() != 'c':
            break
