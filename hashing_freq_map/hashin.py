#Q1 Number Hashing - find the occurance of element in m in n


n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 67, 5, 2]

#method 1 - Brute force

"""""
for num in m:
    count = 0 
    for x in num:
        if x == num:
            count =+ 1
    print(count)
    
"""""   

#method 2 - Optimize

"""""
hash_list[0] 
for num in n:
    hash_list [num] += 1
    
    
for num in m:
    if num <1 or num >10:
        print(0)
    
    else:
        print(hash_list [num])
    
"""



#Q2 Character Hashing - find the occurance of element in m in n

#method 1 - Brute force

#method 2 - Optimize
