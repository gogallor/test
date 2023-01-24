#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import statistics

parser = argparse.ArgumentParser()
parser.add_argument('a', type=str)
args = parser.parse_args()
#print(args.a)


#a = input('введите путь к файлу\n')
nums = []
with open(args.a) as f:
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
