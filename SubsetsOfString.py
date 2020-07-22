#finding subsets of a string using recursion


def solve(ip,op):
    if len(ip)==0:
        print(op)
        return
    op1 = op
    op2 = op
    
    op2+=ip[0]
    ip=ip[1:]
    solve(ip,op1)
    solve(ip,op2)
    return 

solve("abc","")
