from datetime import datetime

def get_birth_date():
    while True:
        birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
        try:
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
            return birth_date
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def calculate_age(birth_date):
    current_date = datetime.now()
    age = current_date - birth_date
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    hours, remainder = divmod(age.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = age.microseconds // 1000
    return years, months, days, hours, minutes, seconds, milliseconds

def main():
    birth_date = get_birth_date()

    try:
        while True:
            age_components = calculate_age(birth_date)
            formatted_age = "You are {:03d} years {:02d} months {:02d} days {:02d} hours {:02d} minutes {:02d} seconds {:03d} milliseconds old".format(*age_components)
            print("\r" + formatted_age, end='', flush=True)
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()
