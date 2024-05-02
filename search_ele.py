#1.Search an element in an array.
#The first line contains two space-separated integers 𝑁 and 𝑋 — the element to be searched.
#The second line contains all the elements of array. 

n,x=map(int, input("Enter the any 2 no.:-").split())
ar=list(map(int,input("Enter array:-").split()))

if x in ar:
    print("yess")
else:
    print("no")