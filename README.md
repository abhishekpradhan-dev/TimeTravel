Time Travel is a Python-based console programme that lets users specify a date and calculates the time difference between that date and the current date. It displays the number of years, months, and days that have passed or will pass between the two dates, giving the impression of time travel.

The project opens with a welcome message to the user, requesting them to enter a date in the "yyyy-mm-dd" format. The input is then parsed and transformed into a datetime object. The current date and time are acquired in Python using the "datetime.now()" function from the "datetime" package.

The code then uses simple arithmetic operations to calculate the time difference between the current date and the entered date. The number of years is determined by dividing the total number of days in the time difference by 365, and the number of months is determined by dividing the remaining days by 30. The number of remaining days is the modulus of the total number of days divided by 30.

Finally, the code shows the calculated years, months, and days to the user as the "time travelled" or "time remaining" depending on whether the entered date is in the past or future. The code also provides some rudimentary error handling to ensure that the user input is in the right date format.


