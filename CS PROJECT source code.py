import pickle

# Define the data file for customer information
data_file = "bank_data.bin"

# Function to initialize the data file with an empty dictionary
def initialize_data_file():
    with open(data_file, "wb") as file:
        pickle.dump({}, file)

# Function to load customer data from the data file
def load_data():
    try:
        with open(data_file, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Function to save customer data to the data file
def save_data(data):
    with open(data_file, "wb") as file:
        pickle.dump(data, file)

# Function to create a new customer account
def create_account(account_number, name, balance):
    data = load_data()
    if account_number not in data:
        data[account_number] = {"name": name, "balance": balance}
        save_data(data)
        print("Account created successfully.")
    else:
        print("Account already exists.")

# Function to deposit funds into an account
def deposit(account_number, amount):
    data = load_data()
    if account_number in data:
        data[account_number]["balance"] += amount
        save_data(data)
        print(f"Deposited ${amount}. New balance: ${data[account_number]['balance']}")
    else:
        print("Account not found.")

# Function to withdraw funds from an account
def withdraw(account_number, amount):
    data = load_data()
    if account_number in data:
        if data[account_number]["balance"] >= amount:
            data[account_number]["balance"] -= amount
            save_data(data)
            print(f"Withdrew ${amount}. New balance: ${data[account_number]['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

# Function to check account balance
def check_balance(account_number):
    data = load_data()
    if account_number in data:
        print(f"Account balance for {data[account_number]['name']}: ${data[account_number]['balance']}")
    else:
        print("Account not found.")

# Function to calculate loan amount
def calculate_loan_amount(principal, rate, time):
    interest = (principal * rate * time) / 100
    return principal + interest

# Function to transfer money between accounts
def transfer(sender_account, receiver_account, amount):
    data = load_data()
    if sender_account in data and receiver_account in data:
        if data[sender_account]["balance"] >= amount:
            data[sender_account]["balance"] -= amount
            data[receiver_account]["balance"] += amount
            save_data(data)
            print(f"Transferred ${amount} from account {sender_account} to account {receiver_account}.")
        else:
            print("Sender account has insufficient balance.")
    else:
        print("One or both accounts not found.")
        

# Function to display fixed deposit details
def fixed_deposit_details(principal, rate, time):
    interest = (principal * rate * time) / 100
    maturity_amount = principal + interest
    print(f"Principal amount: ${principal}")
    print(f"Rate of interest: {rate}%")
    print(f"Time period (in years): {time}")
    print(f"Interest earned: ${interest}")
    print(f"Maturity amount: ${maturity_amount}")

# Main program
if 1>0:
    initialize_data_file()
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. Check Balance")
        print("6. Loan Amount Calculator")
        print("7. Fixed Deposit Details")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            name = input("Enter your name: ")
            balance = float(input("Enter initial balance: "))
            create_account(account_number, name, balance)
            
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            deposit(account_number, amount)
            
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw(account_number, amount)
            
        elif choice == "4":
            sender_account = input("Enter sender's account number: ")
            receiver_account = input("Enter receiver's account number: ")
            amount = float(input("Enter the amount to transfer: "))
            transfer(sender_account, receiver_account, amount)

        elif choice == "5":
            account_number = input("Enter account number: ")
            check_balance(account_number)
            
        elif choice == "6":
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate of interest: "))
            time = float(input("Enter time period (in years): "))
            loan_amount = calculate_loan_amount(principal, rate, time)
            print(f"Loan amount: ${loan_amount}")
            
        elif choice == "7":
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate of interest: "))
            time = float(input("Enter time period (in years): "))
            fixed_deposit_details(principal, rate, time)
            
        elif choice == "8":
            break
        
        else:
            print("Invalid choice. Please try again.")
