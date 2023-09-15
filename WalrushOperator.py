'''
Walrush operator (:=): You can assign a value within an expression by walrush operator.
print((a:=100)+1)
b=1000
print((a:=(b+346)))

walrush operator diye amra ekti expression er moddhye value create and new value
assign korte pari.
c=100
e=(d:=c+101)
g=(f:=e+1+200)
'''
# print((a:=100)+1) #101
# b=1000
# print((a:=(b+346))) #1346

# data=[10,20,30,40]
# i=-1
# while (i:=i+1)<(n:=len(data)):
#     print(data[i])

c=100
e=(d:=c+101)
g=(f:=e+1+200)
# print(g) #402

# while True:
#     ans=input('Do you want to add more?(y/n): ').lower()
#     if ans!='y':
#         break
#     print('Continueing the process!')

#with walrush operator
while (ans:=input('Do you want to add more?(y/n): ')).lower()=='y':
    print('Process continueing!')


