import matplotlib.pyplot as plt 

#create data 
# y axis

gt_runs_per_over = [4, 8, 3, 6, 9, 4, 7, 11, 15, 5, 10, 6, 8, 12, 9, 11, 7, 14, 13, 6]
srh_runs_per_over = [0, 6, 17, 4, 3, 4, 8, 10, 4, 0, 4, 12, 0, 10, 4,0,0,0,0,0]

overs = list(range(1,21)) #create list with value of 1 to 20

plt.figure(figsize=(24,8))
plt.bar(overs,gt_runs_per_over,width=0.8,color='cyan',edgecolor='black')
plt.bar(overs,srh_runs_per_over,width=0.8,color='orange',edgecolor='black')
plt.ylim(0,25)
plt.xlim(1,20)
plt.xticks(ticks=range(1,21),labels=range(1,21))
plt.grid()
plt.legend(['Runs'])
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.show()