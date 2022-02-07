import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from math import factorial, exp, sqrt


type = int(input("(1)Binomial Testing (2)Poisson Testing (3)Normal Testing: "))

if type == 1:

     X = input( "Define the Variable:  ")

     print("P_0 represents the proportion to be tested. ")

     P_0 = float(input("P_0 :  "))

     n = int(input("The sample size :  "))

     L = float(input("Enter significance Level :  "))

     x = int(input("Enter Test Value :  "))

     S = ((factorial(n))/((factorial(x)*(factorial(n-x)))))*(P_0**x)*(1-P_0)**(n-x)
     S_1 = ((factorial(n))/((factorial(x)*(factorial(n-x)))))*(P_0**x)*(1-P_0)**(n-x)
     S_2 = ((factorial(n))/((factorial(x)*(factorial(n-x)))))*(P_0**x)*(1-P_0)**(n-x)

     A = int(input("(1)Increase (2)decrease (3)change: "))

     if A == 1:
        while x <= n:
              S = ((factorial(n))/((factorial(x+1)*(factorial(n-x+1)))))*(P_0**(x+1))*(1-P_0)**(n-x+1) + S
              x += 1
       
        if S < L:
            print("Reject P_0")

        else:
            print("Accept")

     elif A == 2:
         while x > 0:
               S = ((factorial(n))/((factorial(x-1)*(factorial(n-x-1)))))*(P_0**(x-1))*(1-P_0)**(n-x-1) + S
               x -= 1
        
         if S < L:
            print("Reject P_0")

         else:
            print("Accept")

     elif A == 3:
         while x > 0:
               S_1 = ((factorial(n))/((factorial(x-1)*(factorial(n-x-1)))))*(P_0**(x-1))*(1-P_0)**(n-x-1) + S_1
               x -= 1
         while x <= n:
               S_2 = ((factorial(n))/((factorial(x+1)*(factorial(n-x+1)))))*(P_0**(x+1))*(1-P_0)**(n-x+1) + S_2
               x += 1

         if S_1 < L or S_2 < L:
            print("Reject P_0")
         elif S_1 > L and S_2 > L:
            print("Accept")
         else:
            print("Error.")
     else:
        print("Error.")

elif type == 2:

      X = input( "Define the Variable(Do not forget to check for proper proportions):  ")

      print("P_0 represents the mean to be tested. ")

      P_0 = float(input("P_0 :  "))

      L = float(input("Enter significance Level :  "))

      x = int(input("Enter Test Value :  "))

      S = (exp(-P_0))*((P_0**x)/factorial(x))
      S_1 = (exp(-P_0))*((P_0**x)/factorial(x))
      S_2 = (exp(-P_0))*((P_0**x)/factorial(x))

      A = int(input("(1)Increase (2)decrease (3)change: "))

      if A == 1:
         while x <= n:
              S = (exp(-P_0))*((P_0**(x+1))/factorial(x+1)) + S
              x += 1
       
         if S < L:
            print("Reject P_0")

         else:
            print("Accept")

      elif A == 2:
         while x > 0:
               S = (exp(-P_0))*((P_0**(x-1))/factorial(x-1)) + S
               x -= 1
        
         if S < L:
            print("Reject P_0")

         else:
            print("Accept")

      elif A == 3:
         while x > 0:
               S_1 = (exp(-P_0))*((P_0**(x-1))/factorial(x-1)) + S_1
               x -= 1
         while x <= n:
               S_2 = (exp(-P_0))*((P_0**(x+1))/factorial(x+1)) + S_2
               x += 1

         if S_1 < L or S_2 < L:
            print("Reject P_0")
         elif S_1 > L and S_2 > L:
            print("Accept")
         else:
            print("Error.")
      else:
        print("Error.")