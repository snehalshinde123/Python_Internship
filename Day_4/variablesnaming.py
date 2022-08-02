# variable naming convention rules

myvar = "Shiv"
my_var = "Shiv"
_my_var = "Shiv"
myVar = "Shiv"
MYVAR = "Shiv"
myvar2 = "Shiv"

# invlaid variable names
'''
2myvar = "Shiv"
my-var = "Shiv"
my var = "Shiv"
'''

print(myvar)
print(my_var)
print(_my_var)
print(myvar)
print(MYVAR)
print(myvar2)
'''
print(2myvar)
print(my-var)
print(my var)
'''
#Assigning Multiple Values to Multiple Variables

col1, col2, col3 = "red", "orange", "green"
print(col1)
print(col2)
print(col3)

#Assigning one value  to Multiple Variables.

col1= col2= col3="red"

print(col1)
print(col2)
print(col3)

# Assigning vaules from list to variables

colors=["red","yellow","green"]

print("Assinging values from list to vairables")

col1, col2, col3 = colors

print(col1)
print(col2)
print(col3)

# multiple variables in one statement

x = "Shiv "
y = "is "
z = "awesome"

print(x + y + z)
print(x , y , z)

# In case of '+' operator

x = 1000
y = 10
print(x + y)
x = 100
y = "shiv"
print(x + y)