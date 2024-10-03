nums = [1,2,3,5]
nums = list(map(str,nums))
new_nums = []
for i in nums:
    total = 0
    for j in i:
        total += int(j)
    new_nums.append(total)
ans = min(new_nums)
print(ans)