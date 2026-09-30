import timeit

setUp = '''

import random
import math

'''

lastelement = '''
def RandomArray(size):
    a=[]
    for i in range (0,size):
        a.append(random.randint(1,100))
    return a

def Exchange(i, j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp

def LastElementQuickSort(a, p, r):
    #Code quicksort with a LastElementPartition
    if p < r:
        q=LastElementPartition(a,p,r)
        LastElementQuickSort(a,p,q-1)
        LastElementQuickSort(a,q+1,r)
    return a


def LastElementPartition(a, p, r):
    #Create code that pattitions the array using the last element as a pivot
    x=a[r]
    i=p-1
    for j in range (p,r):
        if a[j] < x:
            i+=1
            Exchange(i,j)
    Exchange(i+1,r)
    return i+1
a=RandomArray(1024)
LastElementQuickSort(a,0,len(a)-1)'''


randomelement='''
def RandomArray(size):
    a=[]
    for i in range (0,size):
        a.append(random.randint(1,100))
    return a

def Exchange(i, j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp

def RandomElementQuickSort(a,p,r):
    #Code quicksort with a RandomElementPartition
    if p < r:
        rd=random.randint(p,r)
        temp=a[r]
        a[r]=a[rd]
        a[rd]=temp
        q = RandomElementPartition(a,p,r)
        RandomElementQuickSort(a,p,q-1)
        RandomElementQuickSort(a,q+1,r)
    return a


def RandomElementPartition(a,p,r):
    #Create code that pattitions the array using a random element as a pivot
    x=a[r]
    i=p-1
    for j in range (p,r):
        if a[j] < x:
            i+=1
            Exchange(i,j)
    Exchange(i+1,r)
    return i+1
a=RandomArray(1024)
RandomElementQuickSort(a,0,len(a)-1)'''
        
if __name__ == "__main__":

#Place Testing code Here

    print("LastElement: ", timeit.timeit(setup = setUp, stmt = lastelement, number=10000))
    print("RandomElement: ", timeit.timeit(setup = setUp, stmt = randomelement, number=10000))
  