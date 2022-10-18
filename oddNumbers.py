
def oddNumbers(l, r):
    # Write your code here
    num = l
    oddNumbersArr = []
    for i in range(l , r+1): 
        if num % 2 == 0 :
            pass
        else:
            print(num)
            oddNumbersArr.append(num)
        num+=1
        
    return oddNumbersArr


print(oddNumbers(2,5))