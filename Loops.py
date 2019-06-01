student_names = ["Mark","Anthony","Podrick","Dorothy","Shiv","Kalia","Havanna"]
for name in student_names:
    print(name)

for index in range(5,10,2): # for(i = 5; i < 10; i += 2)
    print(index)

for index in range(5,10): # for(i = 5; i < 10; i++)
    print(index)

for index in range(10): # for(i = 0; i < 10; i++)
    print(index)

for name in student_names:
    if(name is "Dorothy"):
        break
    print(name)

for name in student_names:
    if name is "Dorothy":
        continue
    print(name)

x = 0

while x < 10:
    print("Current Count is {0}".format(x))
    x += 1

my_list = [(1,2),(3,4),(5,6),(7,8),(9,10)]

for (a,b) in my_list: # This is known as tuple unpacking
    print(a) # where we can access individual elements of a tuple without iterating over it
    print(b) # Also works without the parantheses around "a,b"

d = {"key1": "value1", "key2": "value2", "key3": "value3"}

# If we use iterate the for loop over d like "for item in d:", we only get to iterate over keys
# But if we use tuple unpacking, we can access both the key and value as a separate variables
# As d.items() return key, value pairs in tuples like (key, value)

for key, value in d.items():
    print(f"Key {key} has value {value}")

word = "Karan"

# enumerate function is a generator function that generates list of tuples in the format: (index, value)
for index, letter in enumerate(word): 
    print(f"The Letter {letter} appears at index {index}") 

list1 = ["key1","key2","key3"]
list2 = ["value1", "value2", "value3"]

# zip is the generator function that combines multiple lists to give back a list of tupples
# a single tuple contains the element from all the lists
for item1, item2 in zip(list1, list2): 
    print(f"{item1} from list1 corresponds to {item2} from list2") 
    # at the same index position

word = "Hello World"

# List Comprehension in python is basically just flattening the for loop in the next few lines:
# for letter in word:
#    my_list.append(letter)
# we can also perform actions on the first letter below as demonstrated further down
my_list = [letter for letter in word]
print(my_list)

my_list = [num ** 2 for num in range(0,11)]
print(my_list)

# We can aslo append the elements conditionally by adding an If statement:
my_list = [x for x in range(0,11) if x % 2 == 0]
print(my_list)

# Adding an else changes the order slightly
my_list = [x if x % 2 == 0 else 'ODD' for x in range(0,11)]
print(my_list)

# Nested loops can also be used
my_list = [x * y for x in [2,4,6] for y in [1,10,100]]
print(my_list)
# This is similar to:-  
# for x in [2,4,6]:
#     for y in [1,10,1000]:
#         my_list.append(x*y)
