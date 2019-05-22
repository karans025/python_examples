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
