'''
This is not a hackerrank task, but it's an interview question that was asked to my frined in a well known company interview 
So the question is to sepearte the dictionary on the basis of any key
Let's suppose if there's any key whose value is repeating in some other dicts, e.g. we have data of users 
and we want to filter out on the basis of the age, like how many of the same age persons exist in out list of dictionaries, 
so we create a new list of dictionaries and filterout on the basis of the age and put all the dictionaries that include the age 24, 
in a list and assign it to the key which is 24. 


CNVERTING THISSSS

listOfDict = [{"name" : "Shahmeer", "age":24},
{"name" : "Maheer", "age":24},
{"name" : "Qasim", "age":24},
{"name" : "Shabana", "age":25},
{"name" : "Mudasir", "age":25}]

INTO THISSSS

--> [{24:[{"name" : "Shahmeer", "age":24},{"name" : "Maheer", "age":24},{"name" : "Qasim", "age":24}] ,
 25: [{"name" : "Shabana", "age":25}, {"name" : "Mudasir", "age":25}] }]

'''



def filtering(li , filterKey):
    result = []
    for i in li:
        if len(result) == 0: 
            result.append({li[0][filterKey]:[i]})
        else: 
            if i[filterKey] in result[0].keys():
                result[0][i[filterKey]].append(i)
            else: 
                result[0][i[filterKey]] = [i] 
    return result
 

listOfDict = [{"name" : "Shahmeer", "age":24},
{"name" : "Shahmeer", "age":24},
{"name" : "Qasim", "age":24},
{"name" : "Shabana", "age":25},
{"name" : "Mudasir", "age":25}]

'''
--> [{24:[{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24}] ,
 25: [{"name" : "Shabana", "age":25}, {"name" : "Shabana", "age":25}] }]

'''
print(filtering(listOfDict,"age"))



