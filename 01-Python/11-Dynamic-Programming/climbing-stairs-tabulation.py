n = 4
a = 1
b = 1

"1 1 2 3 5 8"
for i in range(n):
    a,b = b,a+b

print("number of ways to climb",n,"stairs is ",a)