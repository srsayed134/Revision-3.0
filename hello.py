# 1. Start python
"""
print("HEllo, World")
"""

# 2. Understand bug
"""
print("Test" -> error
"""

# 3. Variables
"""
name = input("What's your name?")
print("hello,")
print(name);
"""

# 4. Comment (Show an example how comment can work in pseudocode)

"""
#Ask user for name
name = input("Hey, what is your name? ")
# Say hello to user
print("Hello");
print(name)
""" 
# 5. Printing line in one 
"""
name = input("What is your name ");
print("Hello, " + name) # it concate 
"""
"""
name = input("What is your name? ");
print("Hello,", name) # in two arguments python add a space 
"""
# 6. Named Prarmeters

"""
name = input("What's your name?")
print("hello, ", end="") #because of end="" default end="\n" not work
print(name)
"""

"""
name = input("What's your name? ")
print("hello,", name, sep="???") #hello,???David  #wehn i use sep="???" 
"""

#7. Escaping caracter
"""
print("Hello, \"friend\"")
"""

#8.f-string
"""
name = input("What is your name? ") 
print(f"hello, {name}") #in there name consider as dynamicly
"""

# 9. String method
"""
name = input("What is your name ? ")
name = name.strip() # Remove whitespacce from str
# name = name.capitalize() #Capitalize first word
name = name.title() #It isuse for name all word's first later will capital
print(f"hello, {name}")
"""

# also
"""
name = input("What is your name? ")
name = name.strip().title()
print(f"hello, {name}")
"""

# also 
"""
name = input("What is your name? ").strip().title()
print(f"Hello, {name}")
"""

#also
"""
name = input("What is your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first} {last}")
"""
# 10. Integers

#command python word in terminal make tarminal and enviornment writable it it called interactive mode

# z will concate number not adding like math\
"""
x = input("What is x? ")
y = input("What is y? ")
z = x + y
print(z) 
"""

# Now z will convert string to interger and result will mathmatical
"""
x = input("What is x? ")
y = input("What is y? ")
z = int(x) + int(y)
print(z) 
"""

#also
"""
x = int(input("What is x? "))
y = int(input("What is y? "))
print(x + y)
"""

#11. Float
"""
x = float(input("What is x? "))
y = float(input("What is y? "))

print( x + y )
"""
#round to nearest
"""
x = float(input("What is x? "))
y = float(input("What is y? "))
z = round(x + y);

print(z);
"""
#made " , " in big ammount
"""
x = float(input("What is x? "))
y = float(input("What is y? "))
z = round(x + y);

print(f"{z:,}")
"""
#made " , " in big ammount by f string approch
x = float(input("What is x? "))
y = float(input("What is y? "))

z = x / y
print(f"{z:.2f}")







