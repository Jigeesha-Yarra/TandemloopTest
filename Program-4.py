def dictionary_count(nums):
    dic_res = {}
    for i in range(1,10):
        c = 0
        for num in nums:
            if num%i == 0:
                c += 1 
        dic_res[i] = c 
    return dic_res 

nums = [1,2,8,9,12,46,76,82,15,20,30]
result = dictionary_count(nums)
print(result) 