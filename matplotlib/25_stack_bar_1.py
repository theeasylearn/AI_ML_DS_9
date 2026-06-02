import matplotlib.pyplot as plt 
import numpy as np 

congress_seats = [140, 141, 114, 145, 206, 44, 52, 99]

bjp_seats = [161, 182, 182, 138, 116, 282, 303, 240]
# Election years from the 11th to 18th Lok Sabha
lok_sabha_years = [1996, 1998, 1999, 2004, 2009, 2014, 2019, 2024]
plt.figure(figsize=(12,12))
plt.bar(lok_sabha_years,congress_seats,color='green',label='congress')
plt.bar(lok_sabha_years,bjp_seats,bottom=congress_seats,color='orange',label='bjp')
plt.xticks(ticks=lok_sabha_years,labels=lok_sabha_years)
plt.xlabel('loksabha years')
plt.ylabel('seat')
plt.title('BJP and congress comparison')
plt.grid()
plt.legend(loc='upper left')
plt.show()