#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#a = input('введите путь к файлу параметров окружности\n')
#b = input('введите путь к файлу координат точек\n')

a = 'params.txt'
b = 'coordinates.txt'

params = []
with open(a) as f:
    file_input = f.read().split()
    for i in file_input:
        try:
            params.append(float(i))
        except:
            pass

x_0 = params[0]
y_0 = params[1]
rad = params[2]

coordinates = []

with open("coordinates.txt") as f:
    for line in f:
        coordinates.append([float(x) for x in line.split()])     
        
for i in range(len(coordinates)):
    x = coordinates[i][0]
    y = coordinates[i][1]
    h = (x - x_0)**2 + (y - y_0)**2
    if h == rad**2:
        print(0)
    elif h > rad**2:
        print(2)
    else:
        print(1)

