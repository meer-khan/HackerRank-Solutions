def breakingRecords(scores):

    best = worst = scores[0] 
    #  scores[0] 
    bestCount = 0 
    worstCount = 0
    for score in scores: 
        if score > best: 
            best = score 
            bestCount += 1 
        
        elif score < worst: 
            worst = score 
            worstCount += 1 
    
    # print(bestCount , worstCount)
    return [bestCount , worstCount]


breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
