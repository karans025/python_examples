a = 2
b = 3
#Arithmatic Operators
print(a+b) #addition
print(a-b) #substraction
print(a*b) #multiplication
print(a/b) #division (returns float value)
print(a%b) #Modulous
print(a**b) #Exponent
print(a//b) #Floor Division (returns integer value)
#Assinment Operators
a=b
print(a)
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a**=b
print(a)
a//=b
print(a)
#Comparison Operators
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
#Logical Operators
a = 3
b = 5
print(a and b) #In and operations, the number that comes after is printed
print(a or b) #In or operations, the number that comes before is printed
print(not a) #For any number greater than 0, the result is False for this
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)
#Not covering Bitwise Operators, because frankly I've never used them in my life
#Identity Operators
list1 = [1,2]
list2 = [1,2]
print(list1 is list2) #checks Object similarity rather than just data
print(list1 == list2)
print(list1 is not list2)
tupple1 = (1,2)
tupple2 = (1,2)
print(tupple1 is tupple2) #for immutable types, == and is Operators works the same
print(tupple1 == tupple2)
list = [1,2,[3,4,5],(6,7,8),'9']
print(1 in list) # works similar to Exists method in java
print([3,4,5] in list)
tupple = (6,7,8)
print(tupple not in list)
