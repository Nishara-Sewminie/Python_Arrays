l = []
n = int(input("Enter length of list:"))
for i in range(0,n):
    e = int(input("Enter Element:"))
    l.append(e)
print(l)

even = []
odd = []
for j in l:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("Even Element List : ", even, "\n")
print("Odd Element List : ", odd, "\n")

even.sort()
print("Sorted even : ", even, "\n")
x = len(even)
print("The largest number of even is : ", even[x-1], "\n")

odd.sort()
print("Sorted odd : ", odd, "\n")
y = len(odd)
print("The largest number of odd is : ", odd[y-1])

