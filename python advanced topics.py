#question 1
print("<-------- soultion 1 -------->")
l=[]
for i in range (1,11):
    l.append(i*i*i)
print(l)


#question 2
print("<-------- soultion 2 -------->")
l=[x for x in range(2, 20)
     if all(x % y != 0 for y in range(2, x))]
print(l)

#question 3
'''
print("<-------- soultion 3 -------->")
A List Comprehension, just like the plain range function, executes immediately and returns a list.
A Generator Expression, just like xrange returns and object that can be iterated over.
The comparision is not perfect though, because in an object returned by the generator expression, we cannot access an element by index.
The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets [] while the Generator
expression is enclosed in plain parentheses ().
'''

#question 4
print("<-------- soultion 4 -------->")
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit=list(map(lambda x : (x*1.8)+32,Celsius))
print(Fahrenheit)



#question 5

print("<-------- soultion 5 -------->")
l= [1,2,3,4,5]
l1=list(map(lambda x: x**2,l))
print(l1)


#question 6
print("<-------- soultion 6 -------->")
import sympy
num=[1,2,3,4,5,6,7,8,9]
l = list(filter(lambda x: True if sympy.isprime(x) else False, num))
print(l)

#question 7
print("<-------- soultion 7 -------->")
import functools
l=[1,2,3,4,5]
p=functools.reduce(lambda x,y: x*y,l)
print(p)
