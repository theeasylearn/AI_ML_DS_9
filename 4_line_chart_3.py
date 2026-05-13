import matplotlib.pyplot as plt
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
delhi_temp = [14, 18, 24, 30, 35, 34, 31, 30, 29, 26, 20, 15]
ahmedabad_temp = [17, 21, 27, 33, 38, 36, 33, 32, 31, 30, 24, 19]

plt.plot(months,delhi_temp,color='green',marker='o',linewidth='2',label='new delhi',markersize=10,markeredgecolor='black')
plt.plot(months,ahmedabad_temp,color='orange',marker='s',linewidth='2',label='Ahmedabad',markersize=10,markeredgecolor='black')

plt.xlabel('months')
plt.ylabel('average temperature')
plt.title('Comparision of temperature of ahmedabad and new delhi')
plt.grid()
plt.legend()
plt.show()