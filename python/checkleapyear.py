# Default function to implement conditions to check leap year
import time
def CheckLeap(Year):
  # Checking if the given year is leap year
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Given Year is a leap Year");
  # Else it is not a leap year
  else:
    print ("Given Year is not a leap Year")
# Taking an input year from user
Year = int(input("Enter the number: "))
# Printing result


start_time=time.time()
CheckLeap(Year)
end_time=time.time()
print("time taken by the def function:",start_time-end_time)
