list1=[]
n = int(input("Enter number of elements to be entered in the list: "))
print("Enter elements to be entered in list")
for i in range(0,n):
    a = int(input())
    list1.append(a)
for p in list1:
    if p>0:
        print(p,end=" ")
