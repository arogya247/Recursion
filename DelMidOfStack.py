def solve(arr,k):
    if k==1:
        arr.pop()
        return 
    temp = arr.pop()
    solve(arr,k-1)
    arr.append(temp)
    return 

def del_mid(arr,n):
    if len(arr)==0:
        return arr
    k=(n//2)+1 
    solve(arr,k)
    return arr


aha = [6,5,4,3,2,1]

del_mid(aha,6)

print(aha)
