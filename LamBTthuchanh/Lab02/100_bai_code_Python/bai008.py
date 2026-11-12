import math 
a, b, c = map(int, input().split())
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
R = (a*b*c)/(4*S)
print(f'{R:.3f}')