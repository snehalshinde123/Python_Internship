from argparse import REMAINDER


string = "hello i am shiv and i as software engineer"
print(string[0])

print(len(string))

print("software" in string)

string_2 = "10,20,30,40,50"
result="60" in string_2

print(result)
notinresult = "angular" not in string
print(notinresult)

# String slicing

print(string[0:5])

#string slicing from start

print(string[:32])

#string slicing to the End

print(string[3:])

# negative slicing

print(string[-15:-10])

#Engineer positive indexing

'''
Positive Indexing
E n g i n e e r
0 1 2 3 4 5 6 7
'''

# Negative Indexing

'''
E n g i n e e r
-8 -7 - 6 -5 -4  -3 -2 -1
'''
