
accounts = {}

print("Welcome to the Account Management System")
print("Select 1 for creating an account")
print("Select 2 for login")

# Get user selection
select = int(input("Select the option: "))

if select == 1:
    # Account creation
    name = input("Enter your name: ")
    
    # Check if the account already exists
    if name in accounts:
        print("Account already exists. Please log in instead.")
    else:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        
        if password == confirm_password:
            # Store the account with the username and password
            accounts[name] = password
            print("Account created successfully!")
        else:
            print("Error: Passwords do not match. Account creation failed.")
    
elif select == 2:
    # Login
    name = input("Enter your name: ")
    
    # Check if the account exists
    if name in accounts:
        password = input("Enter your password: ")
        
        # Validate the password
        if accounts[name] == password:
            print("Login successful! Welcome back, {}.".format(name))
        else:
            print("Error: Incorrect password. Login failed.")
    else:
        print("Error: Account does not exist. Please create an account first.")
    
else:
    print("Invalid option. Please select either 1 or 2.")