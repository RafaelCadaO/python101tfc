def hellow_world():
    print ("hellow world!")

hellow_world()

def sum(num1=0,num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total  = sum()
print (total)



def multiple_item(*args):
    print(args)
    print(type(args))

multiple_item ("Dave","Jhon","Sara")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gary")


