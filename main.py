import datetime

def time_traveler():
    print("Welcome to the 'Time Travel' ")
    print("Enter Date (yyyy-mm-dd): ")
    date_input = input()

    try:
        travel_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        current_date = datetime.datetime.now()

        if travel_date > current_date:
            print("Nice joke buddy !! LoL")
        else:
            time_difference = current_date - travel_date

            years = time_difference.days // 365
            months = (time_difference.days % 365) // 30
            days = (time_difference.days % 365) % 30

            print("You have traveled to:")
            print(f"Years: {years}")
            print(f"Months: {months}")
            print(f"Days: {days}")
            print("far from today.")

    except ValueError:
        print("Invalid date format. Please enter a date in yyyy-mm-dd format.")

time_traveler()
