# # Kth grammar question leetcode

dic = {1:0,0:1}

def solve(n,k):
    if (n==1 and k==1):
        return 0
    mid = (2**(n-1))//2
    if (k<=mid):
        return solve(n-1,k)
    else:
        temp = solve(n-1,k-mid)
        return (dic[temp])
  
print(solve(4,6))

        
# for i in range(1,9):
#     print(solve(4,i))
