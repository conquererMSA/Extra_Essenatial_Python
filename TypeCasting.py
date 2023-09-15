'''
Type Casting: Converting the value of one data type to another data type.
Python contain two kinds of 'type conversion':
1. Implicit Type Conversion: Python automitically converts data type lower to higher!
 lower=>higher, int=>float=>str
2. Explicit Type Conversion: programmers convert one data type to another

int, float, and complex: Primitive data type
string, List, Tuple: Sequencial data type
Primitive theke sequencial and sequencial theke primitive e data type convert kora
zay na.
Data type er moddhye inter conversion hoy. Tobe number str ke
float and int e convert kora zay.
value1='23.5'
#flaot string ke integer e convert kora zay na.
print(float(value)) #23.5
print(int(value1)) #error:

//complex data type: complex(firstArg, secondArg:optional) function duti argument
recieve kore. complex() function e zodi second argument deya na hoy tobe
defaulvalue/ imagine value 0j dhore ney
'''

value1='23.5'
print(float(value1))
print(complex(float(value1))) # (23.5+0j)