import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

def linearserch(a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            return True
    return False

a=[10,20,50,40,80,90,100]
key=50
if linearserch(a,key):
    print("value found in list")
else:
    print("value not found in list")

x=list(range(1,100000))
plt.plot(x,[y for y in x])
plt.title("Linear searc time complexity is O(n)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()