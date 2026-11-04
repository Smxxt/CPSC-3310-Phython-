def main():
    date_str = input("Enter a date in the format mm/dd/yyyy: ")
    
    parts = date_str.split("/")
    
    if len(parts) != 3:
        print("Error: Date must be in mm/dd/yyyy format with slashes.")
        return
        
    month_str, day_str, year_str = parts
    
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        print("Error: Date must be in mm/dd/yyyy format with slashes.")
        return
        
    month = int(month_str)
    day = int(day_str)
    
    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")
        return
        
    if day < 1 or day > 31:
        print("Error: Day must be between 1 and 31.")
        return
        
    months = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    month_name = months[month]
    print(f"{month_name} {day}, {year_str}")

if __name__ == "__main__":
    main()