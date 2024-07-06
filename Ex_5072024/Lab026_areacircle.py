# program = calculate the area of a circle
# input = radius
import math
#output = area of circle


#data type
#input= int or float =float because it contain pi in formula
#output= float

#formula= pi*r^2

print(math.pi*(float(input("enter the radius\n"))**2))
print("=========================================================================================================")


radius=float(input("enter the radius\n"))
print(math.pi)
area = math.pi*(radius**2)
print(area)