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

name = input("What is your name? ").strip().title()
print(f"Hello, {name}")



