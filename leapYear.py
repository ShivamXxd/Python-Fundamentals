def is_leap_year(year):
  if year % 4 != 0:
    return False
  if year % 100 == 0 and year % 400 != 0:
    return False
  return True

year = int(input("Enter a year: "))
if is_leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")