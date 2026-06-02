import matplotlib.pyplot as plt 
import numpy as np 

players = ['Virat Kohli', 'Rohit Sharma', 'Shubman Gill', 'Shreyas Iyer']
average = [58.72, 48.84, 55.00, 46.00]
errors = [4.1, 4.8, 5.2, 5.5] 

plt.errorbar(players,average,errors,fmt='o',capsize=5,ecolor='red')
plt.xlabel('Players')
plt.ylabel('Average Runs')
plt.title('Indian Player performance')
plt.grid()
plt.show()