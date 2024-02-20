arr = [] 
for i in range(10):
    x = int(input())%42
    arr.append(x)

print(len(set(arr)))