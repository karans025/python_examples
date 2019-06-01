# Python needs no declarations like java, an identifier can be assigned a value directly, no need to declare its type
'''
    This is a multi line comment in python
'''
print("Hello World") # String Data type, Character Data type doesn't exist in python
name = "Karan"
print(len(name)) # lentgh of a string
my_string = "Hello World"
print(my_string[0]) # indexing works in a string as well
print(my_string[1:9:2]) # slicing [start:stop:step] #stop (not including the index number itself) (result here :- el o)
print(my_string[6:]) # Reuslt :- World
print(my_string[:5]) # Result :- Hello
# In both the statements above the space would not be included as space is the 5th index
# We can also call the slicing with just the step size like this :- my_string[::2]
# Like indexing step size can also be negative, my_string[::-1] would just print the string in reverse
# String Concatenation :-
letter = 'z'
letter += 'z'
print(letter + 'z')
letter *= 5
print(letter * 2)
# Split method splits the string it is called upon into a list, it splits the string based on the input passed in the parantheses
print(my_string.split()) # By default split works on white spaces
print(name.split('a')) # But we can split on any letter or sequence of letters
language = "Python"
formattedString = f"Hello {name}, this is {language}"
print(formattedString)
formattedString = "Hello {}, this is {}".format(name, language)
print(formattedString)
formattedString = "Hello {0}, this is {1}".format(name, language)
print(formattedString)
formattedString = "Hello {name}, this is {language}".format(name = name, language = language)
print(formattedString)
float_value = 0.221231123522323124
print("Float value with custom precision: {fv:1.4f}".format(fv = float_value)) # value:width.precision f (width =  whitespaces)
# width is the minimum width the number would take, if there are numbers more than the width, it'll take up that much space
# But if the numbers are less than the width defined, the text would contain whitespaces
# Useful if we need to indent the result with right alignment
a=2 # Identifiers
b=3 # Number Data type: Integer, Decimal, Complex, all are allowed
print(a+b) # Basic std out statement
c = (1,5,6) # Tupple, Differs from List as this is immutable, assigning c[2] = 2 will give an error
d = ((1,2,4), 2, 'eureka!!!!') # Tupple can contain anything, another tupple, a list, integer, string etc.
print(c)
print(d)
e = [1,2,2,5] # List, mutable object, value can be changed, will demonstrate later
print(min(e))
print(max(e))
f = [(1,4,2),[2,4,6,'this is a string'],'this is also a string',False] #Like a tupple, a list can also contain anything
print(e[-1]) # Starts indexing from backwards (last element is -1 indexed)
e.append(6) # Adding an element to a list
print(len(e)) # length of a list
del e[2] # Deleting an element in list
print(e[1:-1]) # Slicing a list, in this example, first and last element are ignored and rest are printed
print(e)
print(f)
e[2] = '3, see, I changed it'
print(e)
g = {"Brief": "This is a dictionary", "Definition": "This is a mutable Key value pair object"}
# JsonObject in java = Dictionary in python
# g["Something"] would  give a KeyError, to avoid that, use
print(g.get("Something", "Unknown")) # This would give "Unknown" as the result, if the "Something" key doesn't exist
print("Keys in g: {0}".format(g.keys()))
print("Values in g: {0}".format(g.values()))
print(f"Key Value Pairs in g: {g.items()}")
print(g)
# Deleting in a dictionary is similar to Lists
print(g["Brief"])
h = {1,2,3,3,4,5,5,6} # Set, Mutable, Ignores Duplicate Elements while printing, don't know about rest of operations as of now
print(h)
