# --*-- coding:utf-8
import math
print('中文')
print('斐波那契数列开始')
maxNum = 10000
fibonacciSeq = []
n = 1
m = 2
fibonacciSeq.append(n)
fibonacciSeq.append(m)
while True:
    c = n + m
    print(n)
    print(m)
    if c < maxNum:
        fibonacciSeq.append(c)
    else:
        break
    n = m
    m = c
print(fibonacciSeq)
