def insertionSort(a):
        for j in range (1, len(a)):
            key=a[j]
            i = j - 1
            while i >= 0 and a[i] > key:
                 a[i+1] = a[i]
                 i =i - 1
            a[i+1]=key
        return a

a=[3,8,9,5,4,2,1]
print(insertionSort(a))

def selectionSort(a, n):
      for i in range(0, n-1):   #c1= n-1
            smallest= i         #c2 = n-1
            for j in range (i+1, n):   #t3=(j)
                  if a[j] < a[smallest]:  #t4=(j-1)
                    smallest = j          #t5=(j-2)
            temp = a[i]              #t6=(j-1)
            a[i]=a[smallest]         #t7=(j-1)
            a[smallest]=temp         #t8=(j-1)


a=[3,8,9,5,4,2,1]
n=len(a)
print(selectionSort(a,n))


     

a=[3,8,9,5,4,2,1]

print("PRINT VALS")



for i in range (len(a)):
     print(a[i])