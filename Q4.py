# Write a Python program to remove duplicates from a list. 
list = [1,1,2,3,4,5,5,10,10,10,10]
UniqueList = []
for i in list:
 if i not in UniqueList:
  UniqueList.append(i)
print("updated list :",UniqueList)