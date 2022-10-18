def getTotalX(a, b):
    firstOfFirst = a[0]
    lastOfFirst = a[-1]
    multiplesArray = []
    GCDArray = []
    if a == [] or b == []:
        return 0
    for i in range(firstOfFirst , lastOfFirst+1): 
        count = 0
        for j in a: 
             if j%i == 0 :
                # multiplesArray.append(i)
                count += 1 
        
        if count == len(a):
            multiplesArray.append(i)

    for i in  multiplesArray:
        count = 0
        for j in b: 
            if j % i == 0: 
                count +=1 
            
        
        if count == len(b): 
            GCDArray.append(i)
    
    return len(GCDArray)


# def getTotalX(a,b):
#     return a_condition(a,b)

    
# def a_condition (a,b):
#     ca=0
#     elligible=[]
#     for i in range(a[-1],b[0]+1):
#         for j in a:
#             if i%j==0:
#                 ca=ca+1
                
#         if ca==len(a):
            
#             elligible.append(i)
#             ca=0
#         else:
#             ca=0
#     return b_condition(a,b,elligible)

    
# def b_condition(a,b,elligible):   
#     d=0                           
#     t=0
#     for p in elligible:          
#         for q in b:
#             if q%p==0:
#                 d=d+1
#         if d==len(b):
#             t=t+1
#             d=0
#         else:
#             d=0
#     return (t)








def gcd(a,b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b / gcd(a, b)

def GCD(terms):
    "Return gcd of a list of numbers."
    result = terms[0]
    for i in range(1, len(terms)):
        result = gcd(result, terms[i])
    return result

def LCM(terms):
    "Return lcm of a list of numbers."
    result = 1
    for t in terms:
        result = lcm(result, t)
    return result

def getTotalX(a, b):
    lcm_value = LCM(a)
    gcd_value = GCD(b)
    counter = 0
    multiple_lcm = lcm_value
    while multiple_lcm <= gcd_value:
        if (gcd_value % multiple_lcm) == 0:
            counter += 1
        multiple_lcm += lcm_value
    return counter

print(getTotalX([2,4] , [16,32,96]))