# -*- coding: utf-8 -*-
"""
@title: Prime Factorization
@function: Enter a number and find all Prime Factors (if there are 
any) and display them
@author: Zhilin
"""
def findprime(n):
    '''
    find all the prime numbers smaller than n
    '''
    num= list(range(2,n+1))
    pnum= list()
    while True:
        a= num[0]
        pnum.append(a)
        for i in num:
            if i%a == 0:
                num.remove(i)
        if num==list():
              break
    return(pnum)

def findfac(n):
    '''
    find all prime factors of the number
    '''
    for i in findprime(n):
        if n%i == 0:
            print(i, end=' ')

def main():
    while True:
        try:
            num= int(input('Please input a number:'))
        except ValueError:
            print('Please input a valid integer.')
            continue
        else:
            findfac(num)
            break
            
main()
         
