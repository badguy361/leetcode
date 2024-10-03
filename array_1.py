nums = [1,2,3,5]
target = 9
ans = {}
index1 = 0
for i in nums:
    index2 = index1 + 1
    for j in nums[index1 + 1 :]:
        if i + j == target:
            ans = {index1, index2}
            print(list(ans))
        index2 += 1
    index1 += 1
print(ans)