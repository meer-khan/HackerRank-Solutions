def birthday(s, d, m):
    '''
    params: 
    s: list of numbers mentioned on the squares of chocolate
    d: total sum
    m: total numbers to create that total sum
    '''
    count = 0
    for i in range (len(s)):
        splittedlen = s[i:] 
        sum = 0
        for j in range(m): 
            if sum > d: 
                break
            try: 
                sum += splittedlen[j]
            except: 
                break
        if sum == d:
            count += 1 
    # print(count)
    return count


# birthday([1,2,1,3,2], 3,2)
# birthday([1,1,1,1,1,1] , 3 , 2)
birthday([4] , 4, 1)
            



