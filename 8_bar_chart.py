import matplotlib.pyplot as plt 
ipl_teams = [
    "Mumbai Indians", 
    "Chennai Super Kings", 
    "Kolkata Knight Riders", 
    "Rajasthan Royals", 
    "Sunrisers Hyderabad", 
    "Gujarat Titans", 
    "Royal Challengers Bengaluru", 
    "Deccan Chargers"
]

# Corresponding title wins for each team
title_wins = [5, 5, 3, 1, 1, 1, 1, 1]

plt.barh(ipl_teams,title_wins,height=0.5,color='yellow')

plt.xlabel('No of title win')
plt.ylabel('Team Name')
plt.show();