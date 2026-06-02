import matplotlib.pyplot as plt 
overs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

scores = [11, 26, 39, 50, 72, 97, 108, 117, 126, 129, 137, 145, 150, 156, 162, 169, 172, 183, 194, 208]

plt.plot(overs,scores)
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.title("Match Score")
plt.show()