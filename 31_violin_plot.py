import matplotlib.pyplot as plt 
import pandas as pd 

#read data from file 
result = pd.read_csv('marks_2.csv').squeeze()
# print(result)
#convert list 
data = [
    result[result['Division']=='A']['Mark'],
    result[result['Division']=='B']['Mark'],
    result[result['Division']=='C']['Mark'],
    result[result['Division']=='D']['Mark'],
]
plt.violinplot(data,showmedians=True,vert=True)
plt.xlabel('Division')
plt.ylabel('marks')
plt.xticks(ticks=range(1,5),labels=['A Divison','B Division','C Division','D Division'])
plt.show()

