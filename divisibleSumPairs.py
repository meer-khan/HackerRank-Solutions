def divisibleSumPairs(n, k, ar):
    '''
    params: 
    n: no. of intergers in the array 
    k: number which is divisor 
    ar: array itself that contains numbers 
    '''

    count = 0 
    index = 0
    for i in range(len(ar), -1 ,-1): 
        
        for j in range(i): 
            try:
                sum = ar[index] + ar[j+1]
            except:
                break
            if sum % k == 0:
                count +=1 
        
        index += 1 
    print(count)

divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2] , )








