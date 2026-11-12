import math 
a, b, c = map(int, input().split())
cv = a + b + c
p = cv/2
dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'{cv:.1f}', f'{dt:.3f}')