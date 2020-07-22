# permutation with case change (lowercase input only)


def solve(ip,op):
    if len(ip)==0:
        print(op)
        return 
    op1 = op
    op2 = op
    op1+=ip[0]
    op2+=ip[0].upper()
    ip = ip[1:]
    solve(ip,op1)
    solve(ip,op2)
    return


solve("ab","")
