#!/usr/bin/env python
# coding: utf-8

# Wat is de kans dat de stukken van een staaf die op twee willekeurige punten zijn gebroken, een driehoek vormen?

# In[ ]:


import random
driehoek=0
for i in range (10000):
    punt=[random.random(),random.random()]
    a,b,c = punt[0],punt[1]-punt[0],1-punt[1]
    if a+b>c and a+c>b and b+c>a:
        driehoek=+1
print(driehoek/10000)


# In[ ]:




