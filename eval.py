from math import *
'''
eval()  function argument hisabe shudhu matro string recieve kore
eval() function parses the string arguments and evaluates it as a python expressions...
eval() function ekti function keo exicute kore dey...
eval() function expression value return kore...
return value zekuno type er hote pare, type expression er upor nirvor kore.
structure of eval(): eval(expression, {global}, {local})
'''
print(eval('3*3'))
print(type(eval('set([1,2,3,4,5]+[4,6])')))
# def password():
#     print('Show password')
# def find_solution():
#     equation=input('Enter your qequation only using x variable: ')
#     x= int(input('Enter value of x variable: '))
#     result=eval(equation)
#     return result
# result=find_solution()
# print(result)

# uses global and locals variables and methods
#global variable y
# y=10
# def count():
#     eq=input('Enter equation with x and y: ')
#     x=int(input('Enter value of x: '))
#     global y
#     result=eval(eq,{'y':y},{'x':x})
#     #1. eval(eq, {}): eval() function e zodi global dict empty take tahole kuno global
#     # variable and method use kora zabe na, name error dibe. Tobe builtin method use
#     # kora zabe.
#     #2.
#     return result
# result=count()
# # print(result)

# def count2():
#     name=input('Enter name: ')
#     x=3
#     y=4
    # global dict e zodi x and y declare kora na thake tahole name error dibe
    # zodi global dict e '__buitins__':None deya take tahole builtin method gulu use
    # kora zabe na. (TypeError: 'NoneType' object is not subscriptable) error dibe
#     result=eval('len(name)*x*y',{'__builtins__':None},{'x':x,'y':y,'name':name})
#     print(result)
# count2()

y=120
x=20
# def count3():
#     a=1
#     b=2
#     name='msa'
#     # global y,x
#     result=eval('(squareRoot(y+x)+a+b)*len(name)',{'squareRoot':sqrt,'y':y,'x':x},
#                 {'a':a,'b':b,'name':name})
#     print(result)
# count3()

def count4():
    a=1
    b=2
    name='msa'
    # global y,x
    #ekhane builtin pi global dict e declare kora hoyeche and local b local dict e
    # declare kora hoyeche. Zodi global dict empty hoto tahole pi er jonno name error
    # dito, Ar zodi local dict empty hoto tahole b er jonno error dito,
    result=eval('pi*4*b',{'pi':pi},{'b':b})
    print(result)
count4()






