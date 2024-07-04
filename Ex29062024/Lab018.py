#in built-functions
#functions- repeat a task-you can use a function many times
#we can use the same function many times
#def hello():
 #   print("hello")
  #  print("hello")
   # print("hello")
 #print(),input(),type(),format(),max(),min(),id(),sum(),avg()
 #strings
name="sara"# Array starts from 0=s, 1=a, 2=r, 3=a in sara ===== INDEX
print(name)
print(type(name))
print(id(name))#id - memory location (memory adddress where it is stored 2661551772928
print(len(name))# length of the string  sara=4 length always start from 1
#to convert string from lower case to uppercase upper() used
name=name.upper()
print(name)
#to convert string from upper case to lower case lower() used
name=name.lower()
print(name)
a=name.count('a')# it will return the number of char in string
print(a)
r=name.count('r')
print(r)
#to find array ( the no of char ) which starts from 0 =====INDEX
print(name[1])# at 1 array its a from sara so it display a
print(name[3])
print(name[4])# out of range
#python is immutable means it can't be changed
#name[0]="p"  it will dispay an error is IndexError: string index out of range