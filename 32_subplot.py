import matplotlib.pyplot as plt 
import pandas as pd 
#create subplot chart which has line chart and bar chart
plt.figure(figsize=(14,12))
plt.subplot(1,2,1)

overs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
scores = [11, 26, 39, 50, 72, 97, 108, 117, 126, 129, 137, 145, 150, 156, 162, 169, 172, 183, 194, 208]

plt.plot(overs,scores)
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.title("Match Score")


plt.subplot(1,2,2)
runs_per_over = [4, 8, 3, 6, 9, 4, 7, 11, 15, 5, 10, 6, 8, 12, 9, 11, 7, 14, 13, 6]
overs = list(range(1,21)) #create list with value of 1 to 20
plt.bar(overs,runs_per_over,width=0.8,color='cyan',edgecolor='black')
plt.ylim(0,25)
plt.xlim(1,20)
plt.xticks(ticks=range(1,21),labels=range(1,21))
plt.grid()
plt.legend(['Runs'])
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.tight_layout
plt.show()
