year=int(input("Enter the year : "))
if year%400==0 or year%4==0 and year%100!=0:
      print("The year is leap year.")
else:
    print("The year is not a leap year.")