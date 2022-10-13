def countApplesAndOranges(s, t, a, b, apples, oranges):
    # house = [i for i in range(s,t+1)]
    # totalDistanceofApples = []
    # totalDistanceofOranges = []
    # for i , j in zip(apples, oranges):
    #     print(i)
    #     totalDistanceofApples.append(abs(i+a)) 
    #     totalDistanceofOranges.append(abs(j+b))
    
    # print(totalDistanceofApples,'\n',totalDistanceofOranges)

    orangeCount = 0 
    appleCount = 0


    for i in apples: 
        if abs(i+a) in range(s,t+1):
            appleCount += 1 
    for i in oranges: 
        if abs(i+b) in range(s,t+1):
            orangeCount += 1 

    # for i , j in zip(totalDistanceofApples, totalDistanceofOranges):
    #     if i in range(s,t+1): 
    #         appleCount += 1
        
    #     elif j in range(s,t+1): 
    #         orangeCount +=1 
    
    print(appleCount)
    print(orangeCount)
    
countApplesAndOranges(7,11 , 5, 15, [-2,2,1], [5,-6])