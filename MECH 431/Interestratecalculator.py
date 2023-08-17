#Interest rate calculator
import math 

mode = input( "1-F/P 2-P/F 3-A/F 4-A/P 5-F/A 6-P/A 7-A/G 8-P/G: Enter number corresponding to factor: ")
n = int(input("N (period under which the interest is compounded; integer only): "))
i = float(input("Effective Interest Rate(%): "))
f = int(input("F (if value is unknown put 0)= "))
p = int(input("P = "))
a = int(input("A = "))
g = int(input("G = "))
i = i/100

if mode == '1':
    factor = (1+i)**n
    f = p*factor
    print(factor)
    print(f)

elif mode == '2':
    factor = (1/((i+1)**n))
    p = f*factor
    print(factor)
    print(p)

elif mode == '3':
    factor = (i/((i+1)**n-1))
    a = f*factor
    print(factor)
    print(a)

elif mode == '5':
    factor = (((i+1)**n-1)/i)
    f = a*factor
    print(factor)
    print(p)

elif mode == '4':
    factor = ((i*(i+1)**n)/((i+1)**n-1))
    a = p*factor
    print(factor)
    print(a)

elif mode == '6':
    factor = 1/((i*(i+1)**n)/((i+1)**n-1))
    p = a*factor
    print(factor)
    print(p)

elif mode == '7':
    factor = ((1/i)-(n/((1+i)**n-1)))
    a = g*factor
    print(factor)
    print(a)
    
elif mode == '8':
    factor = (((i+1)**n-(i*n)-1)/((i**2)*(1+i)**n))
    p = g*factor
    print(factor)
    print(p)

else:
    print("you fucked up")
