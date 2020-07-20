
def insert(arr,temp):
    
    if len(arr)==0 or temp>arr[-1]:
        arr.append(temp)
        return 
    
    val = arr[-1]
    arr[:] = arr[:-1]
    insert(arr,temp)
    arr.append(val)
    return 


def sort1(arr):
    
    if len(arr)==1:
        return
    
    temp = arr[-1]
    arr[:] = arr[:-1]
    sort1(arr)
    insert(arr,temp)
    

def new(arr):
    arr[:]=arr[:-2]
    return 

aha = [3,2,4,5]
sort1(aha)
print(aha)
