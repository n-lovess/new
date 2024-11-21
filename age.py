from datetime import datetime

def calulate_age():
    try:
        dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
        dob = datetime.strptime(dob_input, "%Y-%m-%d")

        today = datetime.now()

        age = today.year - dob.year

        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1

        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please enter the date as YYYY-MM-DD.")

calulate_age()
