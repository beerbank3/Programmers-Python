arr = [str(i+1) for i in range(30)] 
for i in range(28):
    x = str(input())
    arr.remove(x)

for i in arr:
   print(i)