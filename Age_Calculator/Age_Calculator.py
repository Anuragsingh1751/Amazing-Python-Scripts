from datetime import date
import calendar


def calculate_age(birthday):
    today = date.today()

    # Check if the birthdate is in the future
    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."

    # Calculate years, months, and days with proper calendar borrowing.
    year_diff = today.year - birthday.year
    month_diff = today.month - birthday.month
    day_diff = today.day - birthday.day

    # Borrow the number of days from the previous month when needed.
    if day_diff < 0:
        month_diff -= 1
        previous_month = today.month - 1
        previous_year = today.year
        if previous_month == 0:
            previous_month = 12
            previous_year -= 1
        day_diff += calendar.monthrange(previous_year, previous_month)[1]

    # Borrow one year when the remaining month count is negative.
    if month_diff < 0:
        year_diff -= 1
        month_diff += 12

    # Return the age as a formatted string
    age_string = f"Age: {year_diff} years, {month_diff} months, and {day_diff} days"
    return age_string


if __name__ == "__main__":
    print(" Age Calculator By Python")

    try:
        birthYear = int(input("Enter the birth year: "))
        birthMonth = int(input("Enter the birth month: "))
        birthDay = int(input("Enter the birth day: "))
        dateOfBirth = date(birthYear, birthMonth, birthDay)
        age = calculate_age(dateOfBirth)
        print(age)
    except ValueError:
        print("Invalid input. Please enter valid integers for the year, month, and day.")
