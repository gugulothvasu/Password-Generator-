
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "!@#$%^&*()-_=+<>?/"

use_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
use_lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
use_digits = input("Include numbers? (yes/no): ").lower() == "yes"
use_special = input("Include special characters? (yes/no): ").lower() == "yes"

character_pool = ""
if use_upper:
    character_pool += uppercase
if use_lower:
    character_pool += lowercase
if use_digits:
    character_pool += digits
if use_special:
    character_pool += special

if not character_pool:
    print("⚠️ You must select at least one character type!")
else:
    password_length = int(input("Enter desired password length: "))
    

    password = ""
    for i in range(password_length):
        password += character_pool[i % len(character_pool)]  
        
    print("Your secure password:", password)
