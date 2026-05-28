import matplotlib.pyplot as plt 
import numpy as np 
leh = [
    -2, -1, -1, 0, 0, 1, 1, 0, -1, 1, 
     1,  2,  2, 3, 3, 2, 2,  3,  4, 3, 
     3,  4,  5, 4, 4, 5, 6,  5,  6, 7, 7
]

# 2. Mean daily temperature data for Keylong (March 2026) in °C
# 31 single values representing Day 1 to Day 31
keylong = [
    -4, -3, -3, -2, -2, -1,  0, -1, -2, -1, 
     0, -1,  0,  1,  1,  0, -1,  1,  0, -2, 
     0,  1,  2,  1,  2,  3,  3,  2,  3,  4, 4
]
x = range(1,32)

plt.stackplot(x,leh,keylong,labels=['leh','keylong'],colors=['green','blue'])
plt.xlabel('days')
plt.ylabel('temperature')
plt.title('temperature')
plt.grid()
plt.legend(loc='upper left')
plt.show()