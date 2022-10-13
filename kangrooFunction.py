def kangaroo(x1, v1, x2, v2):
    '''
    params: 
        x1: Starting positions of Kangroo 1
        v1: Jump Distance of Kangroo 1 
        x2: Starting position of Kangroo 2 
        v2: Jump Distance of Kangroo 2
    '''
    kangroo1Jump = x1+ v1
    kangroo2Jump = x2 + v2
    jumpCondition = True
    noOfJumps = 0 
    while jumpCondition: 
        if kangroo1Jump == kangroo2Jump: 
            return "YES" 
        noOfJumps += 1 
        kangroo1Jump += v1
        kangroo2Jump += v2

        if noOfJumps  == 20: 
            break
    

    return "NO" 


print(kangaroo(0,2,5,3))
