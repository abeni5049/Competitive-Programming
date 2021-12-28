import math
def numberOfFlagstones(n,m,a):
    return math.ceil(n/a)*math.ceil(m/a)
n,m,a = map(int,input().split())
print(numberOfFlagstones(n,m,a))
        
        