import math
import sys
'''
a = -2.0
b = 2.0
ex = 0.01
ef = 0.01
'''
a = 2.0
b = 3.0
ex = 0.01
ef = 0.01


def function (x):
    #F = x - 10 * math.sin(x)
    F = x**3 + 6*x**2 + 10
    return F


def dihotomiya(A,B,EX,EF):
    a = A
    b = B
    ex = EX
    ef = EF
    while True:
        c = (a + b)/2
        print(c)
        if abs(function(c)) < ef: 
            break
        elif (function(c) * function(a)) < 0:
            a = a
            b = c
            if ((b - a)/2) <ex: break
            else: continue
        else:
            a = c
            b = b
            if ((b - a)/2) <ex: break
            else: continue

if __name__ == "__main__":
	print(dihotomiya(a,b,ex,ef))