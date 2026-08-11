#Q-1)Let x=7 and y=2 . print the results x/y and x//y one below the other ,and add a comment stating which operator always gives a float result.
x=7
y=2
#the first operator that is x/y that is division always gives a float result
print( "division=",x/y)
print("floor division=",x//y)


#Q2)Take a sentence as input and print only its first and last character using indexing.
sentence=input("enter a sentence")
print(sentence[0])
print(sentence[-1])

#Q3)Write a program that correctly copies a list (using slicing or .copy()) so that appending an item to the copy does not affect the original list. Demonstarte both lists after the change

num1=[3,4,5,6,7]
num2=num1.copy()
num2.append(9)
print("original list=",num1)
print("new list=",num2)

#Q4)Write a program to add multiple elements to an existing set in one go using update() with a list of new values.
s1={1,2,3,4,5}
l1=[6,7,8,9]
s1.update(l1)
print("set after adding elements=",s1)
