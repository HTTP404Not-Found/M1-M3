a,b = map(int,input().split())
import math
print(math.gcd(a,b))
print(int((a*b)/math.gcd(a,b)))