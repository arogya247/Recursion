# permutation with spaces

def solve(ip,op):
    if len(ip)==0:
        print(op)
        return
    
    op1 = op + ip[0]
    op2 = op + " " + ip[0]
    ip = ip[1:]
    solve(ip,op1)
    solve(ip,op2)
    return
    
solve("bc","a")
