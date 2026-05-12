import matplotlib.pyplot as plt 
years = list(range(2000, 2025)) #create list of year from 2000 to 2025.
gdp_growth = [
    7.60, 4.82, 3.80, 7.86, 7.92,
    9.28, 9.26, 7.66, 3.90, 7.86,
    10.26, 6.63, 5.45, 6.39, 7.41,
    8.00, 8.26, 7.17, 6.90, 4.18,
    -7.30, 8.90, 6.99, 9.2, 8.2
]


# plt.figure(figsize=(12,8))
plt.figure(figsize=(12,20))
plt.xlim(left=2020,right=2025)
plt.xticks(ticks=range(2000,2025),labels=range(2000,2025))
plt.ylim(-9,12)
plt.plot(years,gdp_growth,color='blue',marker='o')
plt.xlabel("years",fontsize='15')
plt.ylabel("gdp growth",fontsize='15')

plt.title("gdp growth rate between 2000 and 2025",fontsize='24',loc='left',pad=20)
plt.legend(['growth rate'],fontsize='08',loc='best')
plt.grid(which='both')
plt.show()