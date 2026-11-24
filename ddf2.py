from datetime import datetime

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = datetime(year, month, day)

formatted_title = event_title.upper()
formatted_date = event_date.strftime("%B %d, %Y").replace(" 0", " ")
month_name = event_date.strftime("%B")
weekday_name = event_date.strftime("%A")

print("\nFormatted Output:")
print(f"Event: {formatted_title}")
print(f"Date: {formatted_date}")
print(f"Year: {year}")
print(f"Month: {month_name}")
print(f"Day: {day}")
print(f"Weekday: {weekday_name}")
