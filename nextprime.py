# -*- coding: utf-8 -*-
"""
@title: Next Prime Number
@function: Have the program find prime numbers until the user chooses
to stop asking for the next one.
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

def nextprime(n):
    for i in findprime(n):
        yield i

def main():
    g= nextprime(10000)
    while True:
        try:
            choice= ((input('Want the next Prime Number? [y/n]\n')).lower())[0]
        except ValueError:
            print('Please input y/n.')
            continue
        
        if (choice!='y' and choice!='n'):
            continue
        
        if (choice=='y'):
            print(next(g))
        else:
            break

main()




