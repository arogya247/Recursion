# unique subsets of a string


arr = []

def solve(ip,op):
    if len(ip)==0:
        if op not in arr:
            arr.append(op)
        #print(op)
        return arr
    op1 = op
    op2 = op
    
    op2+=ip[0]
    ip=ip[1:]
    solve(ip,op1)
    solve(ip,op2)
    return arr

print(solve("aac",""))
