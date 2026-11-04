def main():
    password = input("Enter a password: ")
    
    is_valid = True
    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        is_valid = False
        
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_only_alnum = password.isalnum()
    
    if not (has_upper and has_lower and has_digit):
        print("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")
        is_valid = False
        
    if not has_only_alnum:
        print("Password may only contain letters and digits (no spaces or symbols).")
        is_valid = False

    if is_valid:
        print("Password is valid.")
    else:
        print("Password is invalid.")

if __name__ == "__main__":
    main()