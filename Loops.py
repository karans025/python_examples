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

for index, letter in enumerate(word): # enumerate function is a generator function that generates list of tuples
    print(f"The Letter {letter} appears at index {index}") # in the format: (index, value)

list1 = ["key1","key2","key3"]
list2 = ["value1", "value2", "value3"]

for item1, item2 in zip(list1, list2): # zip is the generator function that combines multiple lists to give back a list of tupples
    print(f"{item1} from list1 corresponds to {item2} from list2") # a single tuple contains the element from all the lists
    # at the same index position
