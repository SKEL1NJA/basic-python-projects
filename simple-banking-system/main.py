import json

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        if amount <= 0:
            print("Amount must be greater than zero to deposit successfully")
        else:
            self.balance += amount
            print(f"New Balance is {self.balance}")


    def withdraw(self, amount):
        """Removes money from the balance if funds are available."""
        if amount <= 0:
            print("Amount must be greater than zero to withdraw")
        elif amount > self.balance:
            print("Insufficient Balance, can't withdraw")
        else:
            self.balance -= amount
            print(f"New Balance is {self.balance}")

    def get_balance(self):
        """Returns the current balance."""
        return self.balance
    

try:
    with open("account_data.json", "r") as file:
        data = json.load(file)
        my_account = BankAccount(data["owner"], data["balance"])
        print(f"Welcome back, {my_account.owner}!")
except FileNotFoundError:
    # If no file exists, create a new account from scratch
    print("No saved account found. Creating a new account.")
    my_account = BankAccount("Uday", 0.0)


def main():
    while True:
        print("\n--- Welcome to the Bank ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print(my_account.get_balance())
        elif choice == '2':
            try:
                amt = float(input("Enter an amount to add: "))
                my_account.deposit(amt)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '3':
            try:
                amt = float(input("Enter an amount to withdraw: "))
                my_account.withdraw(amt)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '4':
            # Package the account data into a dictionary
            account_data = {
                "owner": my_account.owner,
                "balance": my_account.balance
            }
            
            # Save the dictionary to a JSON file
            with open("account_data.json", "w") as file:
                json.dump(account_data, file)
                
            print("Your data has been saved. Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()