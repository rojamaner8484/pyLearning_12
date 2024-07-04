# list- shooping list
# milk,bread,butter,maggy
# 1.add item
# 2.remove item
# 3. update item
# 4.view item
# 5.exit

shopping_list = ["milk", "bread", "butter", "maggy"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[1])
print(shopping_list[3])
print(shopping_list[-2])

#to add item in list
shopping_list.append("sandwich")# append is function for adding items in end
shopping_list.append("biryani")
print(shopping_list)
shopping_list.insert(2,"paneer")#insert is function for adding items in any position
print(shopping_list)
shopping_list.insert(3,"chiken")
print(shopping_list)

shopping_list.extend(["salt","chips"])
print(shopping_list)
shopping_list.remove("salt")
print(shopping_list)
shopping_list.reverse()
print(shopping_list)
shopping_list.sort()
print(shopping_list)


my_list = [1, 2, 3, 4, 5, True, 3.15, "roja"]
print(type(my_list))#<class 'list'>
