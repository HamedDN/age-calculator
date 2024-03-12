from datetime import datetime, timedelta
import time

def calculate_age(birth_date):
    current_date = datetime.now()
    age_difference = current_date - birth_date

    years = age_difference.days 
    age_difference -= timedelta(days=years*365)
    months = age_difference.days 
    age_difference -= timedelta(days=months*30)
    days = age_difference.days
    hours, remainder = divmod(age_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = age_difference.microseconds
    
    return years, months, days, hours, minutes, seconds, milliseconds

def main():
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    
    while True:
        years, months, days, hours, minutes, seconds, milliseconds = calculate_age(birth_date)
        print(f"You are {years} Y, {months} M, {days} D, {hours} h, {minutes} m, {seconds} s, {milliseconds} ms  old", end='\r')
        time.sleep(0.001)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program.")
