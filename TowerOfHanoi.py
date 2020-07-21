#Tower of Hanoi using Recursion

def solve(n,s,d,h):
    if n==1:
        print("moving plate ",n," from ",s, " to ", d)
        return 
    solve(n-1,s,h,d)
    print("moving plate ",n," from ",s, " to ", d)
    solve(n-1,h,d,s)
    return 

solve(3,"source","destination","helper")
