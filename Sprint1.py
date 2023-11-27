

# This program processes strings and dates based on an employee first name, last name, phone number, current date, satrt date and birthdate.
# It is written from October 19, 2023 - November 1, 2023
# By Benjamin Osemene and Andrew Ohwoka


# Program required inputs


import datetime


EmplyeeFirstName = input("Enter the employee first name:   ")
EmplyeeLastName  = input("Enter the employee last name:    ")
PhoneNum = input("Enter the employee phone number(999-999-9999):   ")
start_date_str = "2016-10-19"
birth_date_str = "1990-12-12"


# Program Constants
RETIREMENT_AGE = 65


# Program Calculations 

EmplyeeFullName = EmplyeeFirstName[0] + "," + EmplyeeLastName

EmplyeeID = EmplyeeFirstName[0]+ EmplyeeLastName[0]+ " -" + PhoneNum[4:]

# We then calculated the current date as required.
Cur_date = datetime.datetime.now() 

# Converting the start date and birth date from strings to datetime  objects we have:
start_date = datetime.datetime.strptime(start_date_str,"%Y-%m-%d")
birth_date = datetime.datetime.strptime(birth_date_str,"%Y-%m-%d")

# We calculated  years of working by taking difference between the two dates rounding to whole number.
Years_of_Working = ((Cur_date - start_date).days // 365)


# We calculated how long till employee retirement rounding to whole number  
Years_Till_Retirement = RETIREMENT_AGE - ((Cur_date - birth_date).days // 365)

# Calculating how long in  days till next birthday. We first calculated the current year.
Cur_Year = Cur_date.year

# Then next birthday is calculated by replacing the year in the birthdate with current year (online source)
Next_birthday = birth_date.replace(year=Cur_Year)

# Difference between the next birthday and  current date will give how long till next birthday.
Days_Till_Next_birthday = (Next_birthday - Cur_date).days

# Program results based on string and date processing 

print(f"Employee full name: {EmplyeeFullName:<9s} ")
print(f"Employee number ID: {EmplyeeID:<8s}")
print(f"Employee years of working: {Years_of_Working:<2d} years")
print(f"Years of retirement: {Years_Till_Retirement:<3d} years")
print(f"Days till the next birthdate: {Days_Till_Next_birthday:<3d} days")







