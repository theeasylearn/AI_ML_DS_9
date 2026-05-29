import matplotlib.pyplot as plt 
import numpy as np 

#create 2d list/array
data = np.array([[50, 29,1],[ 6,  4,  1],[31, 12,  5],[ 7,  8,  2],[ 1,  6,  0]])
# print(data)
players = ['Virat Kohli', 'Shubman Gill', 'Rohit Sharma', 'K L Rahul', 'Rishabh Pant']
plt.imshow(data,cmap='cool',interpolation='nearest')
plt.xlabel('players')
plt.yticks(ticks=np.arange(0,5),labels=players)
plt.xticks(ticks=np.arange(0,3),labels=['ODI','TEST','T20'],rotation='vertical')
plt.colorbar()
plt.tight_layout()
plt.title('top 5 players performance')
plt.show()
