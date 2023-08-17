from Rootfinding import bisection
from Rootfinding import secant
import math

#Find the equation which is equal to zero
# F/P = ((1+i)**n)
# P/F = (1/((1+i)**n))
# A/F = (i/((i+1)**n-1))
# F/A = (((i+1)**n-1)/i)
# A/P = (((i*(i+1)**n)/((i+1)**n-1)))
# P/A = ((((i+1)**n-1))/((i*(i+1)**n)))
# A/G = ((1/i)-(n/((1+i)**n-1)))
# P/G = (((i+1)**n-(i*n)-1)/((i**2)*(1+i)**n))

f = lambda i: 1150 - 170*((((i+1)**8-1))/((i*(i+1)**8))) - 0*(1/((1+i)**12))

#Using the bisection and secant method we can find an approximate solution
#Need to guess a range of values where we think the answer lies (a,b)
# Smaller guess
a = float(input("Smaller interest rate(%) of the guess range: "))
# Larger guess 
b = float(input("Larger interest rate(%) of the guess range: "))

approx_phi = bisection(f,a/100,b/100,25)
approx = secant(f,a/100,b/100,25)
print(approx_phi*100)
print(approx*100)
