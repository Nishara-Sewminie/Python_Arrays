def rev(t):
    n = len(t)
    i = 0
    j = n-1
    while i<j :
        tp = t[i]
        t[i] = t[j]
        t[j] = tp
        i+=1
        j-=1

n = int(input("enter n : "))
lt = []
for i in range(0,n):
    lt.append(int(input()))

print(lt)
rev(lt)
print(lt)
