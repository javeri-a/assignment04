def get_user_info():
    # Asking user for input
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Returning all three pieces of data as a tuple
    return first_name, last_name, email_address

def main():
    # Calling the function to get user info
    user_data = get_user_info()
    
    # Printing the received user data
    print("Received the following user data:", user_data)

# This ensures that main() is called when the script runs
if __name__ == "__main__":
    main()
