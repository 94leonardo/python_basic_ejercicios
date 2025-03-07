# Python program to display calendar

import calendar

year = int(input("Enter the year: "))
mount = int(input("Enter the mount: "))

cal = calendar.month(year, mount)

print(cal)
