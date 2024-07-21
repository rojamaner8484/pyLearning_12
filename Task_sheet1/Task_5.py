# leap year
year = int(input("enter the leap year\n"))

if (year % 4 ==0 and year%100 !=0) or (year% 400==0):
    print("entered year is leap year")

   # print("its not leap year")
else:
    print("it not a leap year")




