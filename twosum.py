def twosum(target,a):
    index=[]
  
    for i in range (0,len(a)):
        for j in range (i+1, len(a)):
            if a[i]+a[j] == target:
                index.append(i)
                index.append(j)
                break
        if len(index)==2:
            break
    return index


a=[1,2,2,2]

print(twosum(4,a))