# File: RecursiveFunctions.py
# Student: Arshia Riaz
# UT EID: ar65892
# Course Name: CS303E
# 
# Date Created: 11/16/2021
# Date Last Modified: 11/19/2021
# Description of Program: This program uses recursive functions to find solutions. 

def sumItemsInList(L):
        if L == []:
                return 0
        else:
                return L[0] + sumItemsInList(L[1:])

def countOccurrencesInList(key,L):
        if L == []:
                return 0
        elif key == L[0]:
                return 1 + countOccurrencesInList(key,L[1:])
        else:
                return countOccurrencesInList(key,L[1:])

def addToN(n):
        if n <= 0:
                return 0
        else:
                return n + addToN(n - 1)

def findSumOfDigits(n):
        if n == 0:
                return 0
        else:
                return n % 10 + findSumOfDigits(n//10)

def decimalToBinary(n):
        c = []
        if n == 0:
                return str(0)
        while n >= 1:
                e = n % 2
                c.append(e)
                n=n//2
        c.reverse()
        for i in c:
                print(i,end="")

def decimalToList(n):
        a = []
        if n < 10:
                return [str(n)]
        if n > 0:
                m = str(n % 10)
                a = decimalToList(n // 10)
                a.append(m)
        return a


def isPalindrome(s):
        if s == '' or len(s) == 1:
                return True
        else:
                return s[0] == s[-1] and isPalindrome(s[1:-1])

def findFirstUppercase(s):
        if len(s) == 0:
                return None
        elif s[0].isupper():
                return s[0]
        else:
                return findFirstUppercase(s[1:])

def findFirstUppercaseIndexHelper(s,index):
        if len(s) == 0:
                return -1
        elif s[0].isupper():
                return index
        else:
                return findFirstUppercaseIndexHelper(s[1:],index + 1)

def findFirstUppercaseIndex(s):
        return findFirstUppercaseIndexHelper(s,0)


