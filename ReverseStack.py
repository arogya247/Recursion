
def insert(arr,k):
    if len(arr)==0:
        arr.append(k)
        return 
    m = arr.pop()
    insert(arr,k)
    arr.append(m)
    return

def rev(arr):
    if len(arr)==1:
        return 
    temp = arr.pop()
    rev(arr)
    insert(arr,temp)
    return 
    
    
aha = [1,2,3,4,5,6]
rev(aha)
print(aha)
