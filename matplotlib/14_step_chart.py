import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(6,25) #hours 6 to 24
y = [
    29, 30, 31, 33, 35, 36, 37, 38, 39,
    38, 37, 35, 33, 32, 31, 31, 30, 29, 28
] # bhavnagar_temp_yesterday 

plt.figure(figsize=(18,12))
plt.step(x,y,where='post',color='red',label='24-05-2026 temperature of bhavnagar city')
plt.title('24-05-2026 temperature of bhavnagar city')
plt.xticks(ticks=x,labels=x)
plt.yticks(ticks=range(20,45),labels=range(20,45))
plt.xlabel('hours')
plt.ylabel('temperature')
plt.show()

