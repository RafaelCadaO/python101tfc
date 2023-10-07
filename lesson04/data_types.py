# string data type

#literal assigment
first = 'rafa'
last = 'cadavid'


print(type(first))
print(type(first) ==str)
print(isinstance(first, str))


#constructor 
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) ==str)
print(isinstance(pizza, str))

#concatenation
fullname = first + " " + last
print (fullname)

fullname += "!"
print (fullname)

#casting
decade = str(1980)
print (type(decade))
print (decade)

statement = "i like rock music from the " + decade + "s."
print (statement)


#multiple line

multiline = '''
hey how are you?              

i was just checking in

                               all good?


'''
print (multiline)

#Escapen expecial caracters

sentence = 'I\'m back at work! \t hey! \n wheres\'s this at\\located?'
print (sentence)


#string methods

print (first)
print (first.lower())
print (first.upper())
print (first)

print (multiline.title())
print (multiline.replace("good","ok"))

print(len(multiline))

multiline += "                                 "
multiline = "                      " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#build a manu

title = "menu".upper()
print (title.center(20,"="))
print ("Coffe".ljust(16, ".") + "$1".rjust(4))
print ("Muffin".ljust(16, ".") + "$2".rjust(4))
print ("Chesecake".ljust(16, ".") + "$4".rjust(4))

#string index values

print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])


#Boolean data metodhs

print(first.startswith("r"))
print(first.endswith("a"))

myvalue= True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#numeric data type
#integrater

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))


#float type
gpa = 3.28
y  = float(1.28)
print (type(gpa))
print (type(y))

# complex type

comp_vale =  3+5j
print (type(comp_vale))
print (comp_vale.real)
print (comp_vale.imag)

#build in functions 

print(abs(gpa))
print(abs(gpa*-1))
print(round(gpa))
print(round(gpa, 1))

import math
print (math.pi)
print (math.sqrt(64))
print (math.ceil(gpa))
print (math.floor(gpa))


#casting

zipcode = "123456"
zip_value = int(zipcode)
print(type(zip_value))

#cast error

#zip_value = int ("New York")