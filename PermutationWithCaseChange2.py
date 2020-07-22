# permutation with case change (upper case letter input also)

def solve(ip,op):
    if len(ip)==0:
        print(op)
        return
    
    if ip[0].isdigit()==False:
        op1 = op
        op2 = op
        
        op1+=ip[0]
        if ip[0].islower()==True:
            op2+=ip[0].upper()
        else:
            op2+=ip[0].lower()
        ip=ip[1:]
        solve(ip,op1)
        solve(ip,op2)
        return
            
    else:
        op1=op
        op1 += ip[0]
        ip=ip[1:]
        solve(ip,op1)
        return
        
solve("A1b2C","")