# array : 
1. two pointer 11 15
2. sliding window 567
3. binary search
4. hash table 3217

# linklist
1. fast and slow pointer 141
2. two pointer 2 206
3. dummy node 24 203

# tree
1. recursive
2. preorder traversal
3. inorder traversal 94
4. postorder traversal
5. layer traversal

# string
1. heapq(priority queue) 767
2. Counter 767

# matrix
1. simulation 3239

# skill
1. stack 946. pop第一個元素 popleft: pop(0)
2. stack 227. 進位邏輯 num = num * 10 + int(c)
3. stack 71. 刪除path中第i個元素 path[:i] + path[i+1:]
4. stack 20. 字典取值 bracket map: {')': '(', ']': '[', '}': '{'} bracket_map.get(c) for c in s
5. string 767. 統計頻率 statics = Counter(s) for key, number in statics.items()
6. heap 215. sort 降序 nums.sort(key=lambda x:-x)
7. heap 347. haap按照第一個元素排序 max_heap=[(-freq,num) for num,freq in Counter(nums).items()] heapq.heapify(max_heap)
8. string 395. all & any 用法 all(value >= k for value in char_index.values()):