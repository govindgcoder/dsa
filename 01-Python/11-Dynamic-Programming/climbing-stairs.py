"""
for 1 stair: 1
for 2 stairs:
    1+1
    2
for 3 stairs:
    1+1+1
    2+1
    1+2
    
for n steps:
    ways to come via n-1 + via n-2
    
=> fibonacci
"""

def steps(n):
    if n==0 or n==1:
        return 1
    return steps(n-1)+steps(n-2)
   
print(steps(5))

mem = {}
def effSteps(n, mem=None):
    if mem is None: 
        mem={}
    if n in mem: 
        return mem[n]
    if n==0 or n==1:
        mem[n]=1
        return 1
    mem[n]= effSteps(n-1, mem) + effSteps(n-2, mem)
    return mem[n]
    
print(effSteps(5))
    