'''
Bitewise Operator: Bitwise operators (&,|, ^, ~, >>, <<) perform bit by bit
operations on binary values of two operands.
Zokhon kuno duti operands er bitwise kora hoy, tokhon integer theke value
gulu binary te convert hoy. Tarpor tader upor binary bitwise operation cole.
Operation hsesh hole binary theke integer value te convert hoy and integer value
return kore.

op1=5 # binary value 00000101
op1=3 # binary value 00000011
'''
op1=5 # binary value 00000101
op2=3 # binary value 00000011

# empersant & bitwise operation
# duti operand er value 1 hole kebol result 1 hobe onnotay result 0 hobe
# print(op1&op2) # 1 00000001

#or | opertoration
#duti operand er moddhye kuno ekti 1 holei result 1 hobe onnothay 0 hobe
# print(op1|op2) # 7 00000111

#xor ^ operation
#duti operand er binary value same hole result hobe 0 onnothay result 1
# print(op1^op2) # 6 00000110

#negation ~ operation
# negation ~ operator single binary valuer er upor kaj kore. Orthat zekuno ekti
# operand er upor kaj kore. Operand er binary value ke reverse kore dey. 0 hole value
# 1 and 1 hole value 0 hoy. Negation operator ekti value er upor kaj kore bole eke
# unary operatoro bola hoy. Er binary value onek boro hoy, tai -integer value return
# kore
# print(~op1) #-6

# left-shift << operator:
#left-shift operator binary value ke argument value onuzaye left er dike shift kore
# dey.Fole left er value gulu hariye zay
# print(op1<<2) #20
# op2=00000011 << 00001100

#left-right >> operator
#left-right operator binary value ke argument value onuzaye right er dike shift kore
# dey.Fole right er value gulu 0 diye fillup hoy
# print(op1>>2) #20
# op2=00000011 <<00000000