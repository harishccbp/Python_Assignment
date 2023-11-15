from datetime import datetime
import pytz  # For handling time zones

# Get the current date and time
current_datetime = datetime.now()

# Define the time zone (in this case, 'Asia/Kolkata' for IST)
time_zone = pytz.timezone('Asia/Kolkata')

# Convert the current datetime to the specified time zone
current_datetime_in_ist = current_datetime.astimezone(time_zone)

# Format the datetime in the desired format
formatted_date = current_datetime_in_ist.strftime('%a %b %d %H:%M:%S %Z %Y')

# Print the formatted date
print("Current Date:", formatted_date
