from hashlib import sha256

def hash_password(password):
    """
    Converts a plain password into a SHA256 hash.
    """
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Checks if the given password (after hashing) matches the stored hash for the provided email.
    Returns True if it matches, False otherwise.
    """
    return stored_logins[email] == hash_password(password_to_check)

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # password
    }

    # Testing login with various email-password combinations
    print(login("example@gmail.com", stored_logins, "word"))         # False
    print(login("example@gmail.com", stored_logins, "password"))     # True
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))   # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))   # False
    print(login("student@stanford.edu", stored_logins, "password"))  # True
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # False

if __name__ == '__main__':
    main()










# 🔐 Problem Statement:
# Tum login system banana chahti ho jo real password save na kare — sirf uska hash save kare.

# Hashing ek technique hoti hai jismein hum kisi bhi input (jaise "password") ko ek long, secure string mein convert karte hain — jise wapas original mein badla nahi ja sakta.

# ⚙️ Program Ka Structure:
# 1. stored_logins:
# Ek dictionary hai jisme:

# keys = emails

# values = hashed passwords

# python
# Copy
# Edit
# stored_logins = {
#     "example@gmail.com": "hashed_password_1",
#     "code_in_placer@cip.org": "hashed_password_2",
#     ...
# }
# 2. hash_password(password):
# Yeh function diya gaya password ko hash karta hai using SHA256.

# Example:

# python
# Copy
# Edit
# hash_password("password") 
# # returns something like: 5e884898da28047151d0e56f8dc6292773603...
# 3. login(email, stored_logins, password_to_check):
# Yeh function check karta hai:

# Kya password_to_check ka hash stored password hash ke barabar hai?

# Agar barabar ho ➜ ✅ return True

# Nahi ho ➜ ❌ return False

# 👀 Example Execution:
# python
# Copy
# Edit
# print(login("example@gmail.com", stored_logins, "password"))
# Yeh check karega:

# "password" ko hash karo.

# Dekho kya woh hashed value "example@gmail.com" ke stored hash ke barabar hai?

# Agar hai ➜ True (correct password)
# Nahi hai ➜ False (wrong password)

# 🖨 Final Output:
# python
# Copy
# Edit
# False       # because "word" is not the password
# True        # because "password" is correct
# True        # "Karel" matches stored hash
# False       # "karel" ≠ "Karel" (case sensitive)
# True        # "password" is correct again
# False       # "123!456?789" is not correct
# ✅ Socha Samajh Ke Point:
# Hum real passwords save nahi karte — sirf unka hashed version store karte hain. Jab user login kare, toh uska diya gaya password hash karke match karte hain.

# Agar tum chaho toh main live example ya animation style se bhi samjha sakti hoon — just say the word! 💫








