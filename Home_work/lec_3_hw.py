# -*- coding: utf-8 -*-
"""Copy of lec 3 HW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BckfxmxLa4IbOozvGo66ItEADXsN033s

Q1 Write a Python program that accepts a string from user. Your program should create and display a new string where the first and last characters have been exchanged.

For example if the user enters the string 'HELLO' then new string would be 'OELLH'
"""

a=input("Enter a string")
b=a[0]
c=a[-1]
d=a[1:-1]
print(c+d+b)

"""Q2 Write a Python program that accepts a string from user. Your program should create a new string in reverse of first string and display it.

For example if the user enters the string 'EXAM' then new string would be 'MAXE'
"""

b=input("enter a string")
c=b[ : : -1]
print(c)

"""Q3 Write a Python program that accepts a string from user. Your program should create a new string by shifting one position to left.

For example if the user enters the string 'examination 2021' then new string would be 'xamination 2021e'
"""

user=input("enter a string")
c=user[0]
d=user[1: : ]
print(d+c)

"""Q4 Write a Python program to calculate the length of a string."""

user1=input("enter a string")
print(len(user1))

"""Q5 Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

string=input("enter a string")
start=string[0:2:1]
end=string[ -2::]
a=len(string)
print(a)
if a>=2:
  print(start+end)
if a<2:
  print("empty")

"""Q6 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

nsh

string=input("enter a string")
a=len(string)
b=string[ -3 : : ]
if a<3:
  print(string)

elif b != "ing"   :
     print(string+"ing")
else:
     print(string+"ly")

"""Q7 Write a Python program to remove the nth index character from a nonempty string."""

string=input("enter a string")
n=int(input("enter a index"))
a=string[:n:]
b=string[n+1: :]
print("modified string",a+b)

"""Q8 Write a Python program to change a given string to a newly string where the first and last chars have been exchanged."""

a=input("Enter a string")
b=a[0]
c=a[-1]
d=a[1:-1]
print(c+d+b)

"""Q9 Write a Python script that takes input from the user and displays that in upper and lower cases."""

user=input("enter a string")
s=print(user.upper())
b=print(user.lower())

"""Thank You"""