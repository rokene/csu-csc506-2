#!/usr/bin/env python3

# recursive
def FibonacciNumber(termIndex):
   if termIndex == 0:
     return 0
   elif termIndex == 1:
      return 1
   else:
      return FibonacciNumber(termIndex - 1) + FibonacciNumber(termIndex - 2)

# dynamic
def FibonacciNumberDynamic(termIndex):
   if termIndex == 0:
      return 0

   previous = 0
   current = 1
   i = 1
   while i < termIndex:
      next = previous + current
      previous = current
      current = next
      i = i + 1

   return current
