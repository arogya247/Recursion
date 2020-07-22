# permutation with case change (upper case letter input also)

def solve(ip,op):
    if len(ip)==0:
        print(op)
        return
    
    if ip[0].isalpha()==True:
        op1 = op
        op2 = op
        
        op1+=ip[0].lower()
        op2+=ip[0].upper()
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



solve("A1b2","")
    

