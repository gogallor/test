#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = input('введите путь к файлу\n')
nums = []
with open(a) as f:
    file_input = f.read().split()
    for i in file_input:
        try:
            nums.append(int(i))
        except:
            pass
#print(nums)

m = statistics.median(nums)
#print(m)
print(int(sum(abs(v - m) for v in nums)))

