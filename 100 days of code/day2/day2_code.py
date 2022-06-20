# second day of code
# this is about data types and some fstring 



#the following data types are covered in this Section 

#strings 




print("hello"[1])     #this is called subscripting, using the index of the string to get the character
print("123" + "245")   #this is still a string

#Integers - these are whole numbers 
print(123 + 245)   #this actuallt prints the sum of the two numbers


#Floats - another data type that represents decimal values

print(123_456.21)   # this is thw same as 123456.21
                    #the uderscore are just for visibility

#Boolean    #this is a true and false statements

True      #same as 1 which is binary
False     #same as 0 which is binary


#to get the data type of a value
name = "Naima"
print(type(name))     #this prints string

#when trying to manipulate or use a method for the wrong data type we get the error
TypeError 

#typecasting - converting data type of one variable to another
print("hello " + str(123))


#you can use the type function to inspect the data type we are working with.

#precedence
print(3-3 + 3/3 * 3)

# excercise BM1 CALCULATOR WEIGHT/HEIGHT^2


#rounding numbers using round function 
print(round(7/3, 2))    # the second parameter is the number of decimal places/ digits of precesion, by default round function rounds it to a whole number

#f-srings  -> allows you to concaentate string with values of other data types without doing manual type conversion

name = "Fatima"
height = 1.94
weight = 90
isFemale = True

print(f"{name} is a student whose height is {height}, weight is {weight} and is a {isFemale}")


