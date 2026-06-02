import matplotlib.pyplot as plt 
overs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

scores = [11, 26, 39, 50, 72, 97, 108, 117, 126, 129, 137, 145, 150, 156, 162, 169, 172, 183, 194, 208]

# plt.figure(figsize=(12,8))
plt.figure(figsize=(12,24))
plt.xlim(left=1,right=20)
plt.xticks(ticks=range(1,21),labels=range(1,21))
plt.ylim(0,300)
plt.plot(overs,scores)
plt.xlabel("Overs",fontsize='18',fontweight='bold')
plt.ylabel("Runs",fontsize='18',fontweight='bold')
plt.title("Match Score",fontsize='24',loc='left',pad=20)
plt.legend(['runs'],fontsize='08',loc='best')
plt.grid(which='both')
plt.show()