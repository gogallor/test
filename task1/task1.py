#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('n', type=int)
parser.add_argument('m', type=int)
args = parser.parse_args()

#n, m = map(int, input().split())

i = 1
while True:
    print(i, end='')
    i = 1 + (i + args.m - 2) % args.n
    if i == 1:
        break
print()

