#Count number of occurrences
#eg:-Input: Arr = {1, 1, 2, 2, 2, 2, 3},  X = 2.
#Output: 4

li=list(map(int,input("Enter the array:-").split(',')))
x = int(input("Enter the value to search for: "))
count=0
for ele in li:
    if ele==x:
        count=count+1
print("{} has occured {}".format(x,count))
    
