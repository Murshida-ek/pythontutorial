def consecutive_num(num):
    num_set=set(num)
    longest=0

    for num in num_set:
        if num-1 not in num_set:
            current_num=num
            current_streak=1
            while current_num +1 in num_set:
                 current_num+=1
                 current_streak+=1
            longest=max(longest,current_streak)
    return longest
nums=[100,101,102,103,104,105,1,2,3,4]
print(consecutive_num(nums))

print ("hello world")